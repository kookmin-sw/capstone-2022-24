"""APIs of applies application"""
# pylint: disable=R0901
from applies.models import LeaderApply, MemberApply
from applies.serializers import (
    LeaderApplySerializer,
    LeaderCancelSerializer,
    MemberApplySerializer,
    MemberCancelSerializer,
)
from config.exceptions.input import (
    BadFormatException,
    InvalidProviderIdException,
    NotSupportedProviderException,
)
from config.mixins import MultipleFieldLookupMixin
from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import (
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
    inline_serializer,
)
from mileages.serializers import MileageSerializer
from payments.models import Payment
from payments.serializers import PaymentSaveSerializer
from providers.models import Provider
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from users.serializers import UserMileageSerializer


@extend_schema_view(
    create=extend_schema(
        tags=["Priority-1", "Group"],
        operation_id="모임원 신청",
        request=inline_serializer(
            name="MemberApplyRequestSerializer",
            fields={
                "providerId": serializers.IntegerField(),
            },
        ),
        responses={
            201: OpenApiResponse(
                description="모임원 신청 성공",
                response=inline_serializer(
                    name="MemberApplyResponseSerializer", fields={"member_apply_id": serializers.IntegerField()}
                ),
            )
        },
    ),
    update=extend_schema(
        tags=["Priority-1", "Group"],
        operation_id="모임원 취소",
        request=inline_serializer(
            name="LeaderApplyRequestSerializer",
            fields={
                "memberApplyId": serializers.IntegerField(),
                "cancel": serializers.BooleanField(),
            },
        ),
        responses={200: OpenApiResponse(description="모임원 취소 성공", response=MemberCancelSerializer)},
    ),
)
class MemberApplyViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    """Class for member, leader  apply to Group"""

    serializer_class = MemberApplySerializer
    queryset = MemberApply.objects.select_related(
        "provider",
        "user",
        "payment",
    )
    lookup_fields = ("user_id", "provider_id")

    def apply_member(self, request):
        """Method: process applying Group for Member"""
        # --- 신청 가능 여부 검사
        # 권한 체크 ㅇ
        # 신청 가능한 모임인지 확인(provider.charge != null) (o)
        # 모임원 신청 중복 검사
        # 모임장 신청 중복 검사
        # 구성원 참여 중복 검사
        # --- 마일리지 차감
        # payment가 null이면 total_mileages에서 provider.charge.serviceChargePerMember만큼 차감
        # --- 모임원 신청
        # member_apply에 등록
        # --- 매칭
        # 모임원 신청한 Provider id 받아오기
        # provider(id=provider_id).charge.numberOfSubscribers 받아오기
        # 모임 인원수: leader:1, member:numberOfSubcribers-1
        # 매칭 여부 확인: member_apply와 leader_apply에서 해당 인원수 충족하는지 검사
        # 충족
        # --> *** 신청한 user, leader/member, payment를 leader/member queryset에 저장해두기 ***
        # --> 모임(provider=provider_id인 객체, status="Recruited") 객체 생성
        # --> 구성원 객체(provider, user, payment) x 구성원수 생성  # TODO: leader/member 생성 시 fellow 자동 생성?
        # --> user, provider로 모임원 신청, 모임장 신청 조회
        # --> 일괄 삭제
        # 미충족
        # --> 냅둔다

        _provider_queryset = Provider.objects.prefetch_related(
            "charge", "charge__subscription_type"
        )  # type: QuerySet[Provider]
        _data = request.data
        _user = request.user
        provider_id = _data["provider_id"]
        payment_id = _data["payment_id"]
        try:
            _provider = _provider_queryset.get(id=provider_id)  # type: Provider
            _payment = Payment.objects.filter(Q(id=payment_id))
            # validate provider is supported
            if not hasattr(_provider, "charge"):
                raise NotSupportedProviderException()
        except KeyError as e:
            raise InvalidProviderIdException() from e
        except Provider.DoesNotExist as e:
            raise BadFormatException() from e
        except Payment.DoesNotExist as e:
            raise BadFormatException() from e

        member_apply_serializer = MemberApplySerializer(data={"apply_date_time": timezone.now()})

        if member_apply_serializer.is_valid():
            member_apply_serializer.save(user=_user, payment=_payment, provider=_provider)

        return Response({"member_apply_id": member_apply_serializer.data["id"]}, status=status.HTTP_201_CREATED)

    def cancel_member(self, request):
        """Method: process Cancling Group and refunding for Member"""
        # --- 취소 가능 여부 검사
        # 권한 체크
        # 모임원 신청 기록 확인
        # --- 마일리지 환금
        # payment == null -> total_mileages를 provider.charge.serviceChargePerMember만큼 ++
        # payment != null -> total_mileages를 payment.amount만큼 ++
        # --- 모임원 신청 객체 삭제
        # member_apply 객체 삭제
        _user = request.user
        cancel = request.data.get("cancel")
        member_apply_id = request.data.get("member_apply_id")
        if cancel:
            try:
                _member_apply = MemberApply.objects.get(Q(id=member_apply_id))
            except MemberApply.DoesNotExist as e:
                # 따로 다른 에러 붙여줘도 될듯
                raise BadFormatException() from e
        else:
            # 임시 처리인데 cancel이 의미가 있는지 모르겠네요?
            raise BadFormatException()

        _amount = _member_apply.payment.amount
        user_serializer = UserMileageSerializer(_user, data={"total_mileages": _user.total_mileages + _amount})
        mileage_serializer = MileageSerializer(data={"amount": (-1) * _amount, "renewal_date_time": timezone.now()})
        payment_serializer = PaymentSaveSerializer(
            data={
                "amount": _amount,
                "content": "Mileage",
                "category": "N",
                "method": "V",
                "status": "C",
                "approval_date_time": timezone.now(),
            }
        )
        if (
            mileage_serializer.is_valid(raise_exception=True)
            & payment_serializer.is_valid(raise_exception=True)
            & user_serializer.is_valid(raise_exception=True)
        ):
            mileage_serializer.save(user=_user)
            payment_serializer.save()
            user_serializer.save(total_mileages=(_user.total_mileages + _amount))

        member_cancel_serialzer = MemberCancelSerializer(
            data={
                "user_id": _user.id,
                "payment_id": payment_serializer.data["id"],
                "provider_id": _member_apply.provider.id,
            }
        )
        if member_cancel_serialzer.is_valid():
            _member_apply.delete()

        return Response(member_cancel_serialzer.data, status=status.HTTP_200_OK)


class LeaderApplyViewSet(viewsets.ModelViewSet):
    """Leader apply apis"""

    @extend_schema(
        tags=["Priority-1", "Group"],
        operation_id="모임장 신청",
        request=inline_serializer(
            name="LeaderApplyRequestSerializer",
            fields={"providerId": serializers.IntegerField()},
        ),
        responses={
            201: OpenApiResponse(
                description="모임장 신청 성공",
                response=inline_serializer(
                    name="LeaderApplyResponseSerializer", fields={"leader_apply_id": serializers.IntegerField()}
                ),
            )
        },
    )
    def apply_leader(self, request):
        """Method: process applying Group for Leader"""
        _user = request.user
        provider_id = request.data["provider_id"]

        try:
            _provider = Provider.objects.get(Q(id=provider_id))
        except Provider.DoesNotExist as e:
            raise BadFormatException() from e

        leader_apply_serializer = LeaderApplySerializer(data={"apply_date_time": timezone.now()})
        if leader_apply_serializer.is_valid():
            leader_apply_serializer.save(user=_user, provider=_provider)

        return Response({"leader_apply_id": leader_apply_serializer.data["id"]}, status=status.HTTP_201_CREATED)

    @extend_schema(
        tags=["Priority-1", "Group"],
        operation_id="모임장 취소",
        request=inline_serializer(
            name="LeaderApplyRequestSerializer",
            fields={
                "accessToken": serializers.CharField(),
                "LeaderApplyId": serializers.IntegerField(),
                "cancel": serializers.BooleanField(),
            },
        ),
        responses={200: OpenApiResponse(description="모임장 취소 성공", response=LeaderCancelSerializer)},
    )
    def cancel_leader(self, request):
        """Method: process Cancling Group for Leader"""
        _user = request.user
        leader_apply_id = request.data["leader_apply_id"]
        cancel = request.data["cancel"]
        if cancel:
            try:
                _leader_apply = LeaderApply.objects.get(Q(id=leader_apply_id))
            except LeaderApply.DoesNotExist as e:
                # 따로 다른 에러 붙여줘도 될듯
                raise BadFormatException() from e
        else:
            # 임시 처리인데 cancel이 의미가 있는지 모르겠네요?
            raise BadFormatException()

        leader_cancel_serialzer = LeaderCancelSerializer(
            data={"user_id": _user.id, "payment_id": None, "provider_id": _leader_apply.provider.id}
        )
        print(leader_cancel_serialzer.is_valid())
        if leader_cancel_serialzer.is_valid():
            _leader_apply.delete()

        return Response(leader_cancel_serialzer.data, status=status.HTTP_200_OK)
