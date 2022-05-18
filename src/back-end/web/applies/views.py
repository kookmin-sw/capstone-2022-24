"""APIs of applies application"""

from applies.models import LeaderApply, MemberApply
from applies.serializers import (
    LeaderApplySerializer,
    LeaderCancelSerializer,
    MemberApplySerializer,
    MemberCancelSerializer,
)
from config.exceptions.input import BadFormatException
from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiResponse, extend_schema, inline_serializer
from mileages.serializers import MileageSerializer
from payments.models import Payment
from payments.serializers import PaymentSaveSerializer
from providers.models import Provider
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from users.serializers import UserMileageSerializer


class GroupApplyView(viewsets.ViewSet):
    """Class for member, leader  apply to Group"""

    @extend_schema(
        tags=["Priority-1", "Group"],
        operation_id="모임원 신청",
        request=inline_serializer(
            name="MemberApplyRequestSerializer",
            fields={
                "accessToken": serializers.CharField(),
                "providerId": serializers.IntegerField(),
                "paymentId": serializers.IntegerField(),
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
    )
    def apply_member(self, request):
        """test"""
        _user = request.user
        provider_id = request.data["provider_id"]
        payment_id = request.data["payment_id"]
        try:
            _provider = Provider.objects.get(Q(id=provider_id))
            _payment = Payment.objects.get(Q(id=payment_id))
        except Provider.DoesNotExist as e:
            raise BadFormatException() from e
        except Payment.DoesNotExist as e:
            raise BadFormatException() from e

        member_apply_serializer = MemberApplySerializer(data={"apply_date_time": timezone.now()})

        if member_apply_serializer.is_valid():
            member_apply_serializer.save(user=_user, payment=_payment, provider=_provider)

        return Response({"member_apply_id": member_apply_serializer.data["id"]}, status=status.HTTP_201_CREATED)

    @extend_schema(
        tags=["Priority-1", "Group"],
        operation_id="모임장 신청",
        request=inline_serializer(
            name="LeaderApplyRequestSerializer",
            fields={"accessToken": serializers.CharField(), "providerId": serializers.IntegerField()},
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
        """test"""
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
        operation_id="모임원 취소",
        request=inline_serializer(
            name="LeaderApplyRequestSerializer",
            fields={
                "accessToken": serializers.CharField(),
                "memberApplyId": serializers.IntegerField(),
                "cancel": serializers.BooleanField(),
            },
        ),
        responses={200: OpenApiResponse(description="모임원 취소 성공", response=MemberCancelSerializer)},
    )
    def cancel_member(self, request):
        """test"""
        _user = request.user
        member_apply_id = request.data["member_apply_id"]
        cancel = request.data["cancel"]
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
        """test"""
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
