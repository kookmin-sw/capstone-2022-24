"""APIs of applies application"""
# pylint: disable=R0901,R0914,R0912
from collections import Counter

from applies.exceptions import (
    ApplyAlreadyExistException,
    ApplyFellowTypeNotMatchedException,
    ApplyNotFoundException,
)
from applies.models import GroupApply
from applies.schemas import GROUP_APPLY_POST_EXAMPLE
from applies.serializers import GroupApplySerializer
from config.exceptions.input import (
    AlreadyJoinedGroupException,
    BadFormatException,
    InvalidProviderIdException,
    NotEnoughSubscriptionInformationException,
    NotSupportedProviderException,
)
from config.exceptions.result import ResultNotFoundException
from config.mixins import MultipleFieldLookupMixin
from django.db import IntegrityError
from drf_spectacular.utils import (
    OpenApiResponse,
    extend_schema,
    extend_schema_view,
    inline_serializer,
)
from fellows.models import Leader, Member
from fellows.views import create_fellows_and_map_into_group_by_applies
from groups.views import create_group_with_provider
from mileages.views import create_histories_and_update_mileages
from payments.models import Payment
from providers.exceptions import ProviderNotFoundException
from providers.models import Charge, Provider, SubscriptionType
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response


@extend_schema_view(
    operation_id="모임 신청",
)
class GroupApplyViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    """Class for member, leader  apply to Group"""

    serializer_class = GroupApplySerializer
    queryset = GroupApply.objects.select_related(
        "provider",
        "user",
        "payment",
    ).prefetch_related("provider__charge", "provider__charge__subscription_type")
    http_method_names = ["post", "put"]
    lookup_fields = ("user_id", "provider_id")

    def get_number_of_remain_fellows_in(self, provider: Provider):
        """Get number of fellows by subscription detail and user request"""
        _total_fellows = provider.charge.number_of_subscribers - 1
        _needed_leader = 1
        _needed_members = _total_fellows - _needed_leader
        return {"L": _needed_leader, "M": _needed_members}

    def apply(self, request, apply_type, *args, **kwargs):
        """Method: process applying Group for Member"""
        # --- 1. 신청 가능 여부 검사
        # 1-1. 권한 체크 ㅇ
        # 1-2. 신청 가능한 모임인지 확인(provider.charge != null) ㅇ
        # 1-3. 모임원 신청 중복 검사 - GroupApply 존재 여부 확인 -> 시리얼라이저 ㅇ
        # 1-4. 모임장 신청 중복 검사 /
        # 1-5. 구성원 참여 중복 검사 ㅇ
        # --- 2. 모임원 신청 ㅇ
        # 3-1. member_apply에 등록
        # --- 3. 마일리지 차감 ㅇ
        # 2-1. payment가 null이면 total_mileages에서 provider.charge.serviceChargePerMember만큼 차감
        # --- 4. 매칭
        # 4-1. 모임원 신청한 Provider id 받아오기
        # 4-2. provider(id=provider_id).charge.numberOfSubscribers 받아오기
        # 4-3. 모임 인원수: leader:1, member:numberOfSubcribers-1
        # 4-4. 매칭 여부 확인: member_apply와 leader_apply에서 해당 인원수 충족하는지 검사
        # --- 5. 매칭 여부에 따른 분기
        # 5-1. 충족
        # --> 5-1-1. *** 신청한 user, leader/member, payment를 leader/member queryset에 저장해두기 ***
        # --> 5-1-2. 모임(provider=provider_id인 객체, status="Recruited") 객체 생성
        # --> 5-1-3. 구성원 객체(provider, user, payment) x 구성원수 생성  # TODO: leader/member 생성 시 fellow 자동 생성?
        # --> 5-1-3. user, provider로 모임원 신청, 모임장 신청 조회
        # --> 5-1-4. 일괄 삭제
        # 5-2. 미충족
        # --> 냅둔다
        _fellow_type_class = Member if apply_type == "M" else Leader
        _provider_queryset = Provider.objects.prefetch_related(
            "charge", "charge__subscription_type", "group_set", "group_set__fellow_set", "group_set__fellow_set__user"
        )  # type: QuerySet[Provider]
        _user = request.user
        _use_mileage = True
        _payment = None
        try:
            _provider = _provider_queryset.get(id=request.data["provider_id"])  # type: Provider
            # if payment is not none
            if "payment_id" in request.data and request.data["payment_id"] is not None:
                # disable mileage use && validate payment
                _use_mileage = False
                _payment = Payment.objects.get(id=request.data["payment_id"])  # type: Provider
            # validate provider is supported
            if not hasattr(_provider, "charge"):
                raise NotSupportedProviderException()
            # check user already joined in group of the provider
            if bool(_provider.group_set.filter(provider=_provider, fellow__user=_user)):
                raise AlreadyJoinedGroupException()
            # use mileages if payment is null
            if not _payment and apply_type == "M":
                _amount = _provider.charge.service_charge_per_member
                # _mileage_response = MileageViewSet.as_view({"post": "partial_update"})(_mileage_request)
                create_histories_and_update_mileages(request, -_amount)
            # apply groupx
            _response = super().create(request, args, kwargs)
            # check group is recruited
            _num_of_needed_fellows = self.get_number_of_remain_fellows_in(_provider)
            _matched_applies = self.get_queryset().filter(provider__id=_provider.id).all()
            # Recruited !!!!!!!
            # format ex. {"L": 1, "M": 2}
            if _num_of_needed_fellows == dict(Counter(_matched_applies.values_list("fellow_type", flat=True))):
                # 5-1-2. create group
                _new_group = create_group_with_provider(provider=_provider)
                # 5-1-3. create fellows and map leader / member by each fellow_type
                _other_fellows_with_type = create_fellows_and_map_into_group_by_applies(
                    _new_group, queryset=_matched_applies
                )
                # 5-1-4.
                _matched_applies.delete()
            return _response
        except TypeError as type_error:
            raise BadFormatException() from type_error
        except KeyError as key_error:
            raise InvalidProviderIdException() from key_error
        except Provider.DoesNotExist as provider_error:
            raise ProviderNotFoundException() from provider_error
        except Payment.DoesNotExist as payment_error:
            raise BadFormatException() from payment_error
        except Charge.DoesNotExist as charge_error:
            raise NotEnoughSubscriptionInformationException() from charge_error
        except SubscriptionType.DoesNotExist as subscription_error:
            raise NotEnoughSubscriptionInformationException() from subscription_error
        except IntegrityError as error:
            raise ApplyAlreadyExistException() from error

    @extend_schema(
        tags=["Priority-1", "Group"],
        operation_id="모임원 신청",
        description="Apply member of provider(id={provider_id})",
        request=inline_serializer(
            name="GroupApplyRequest", fields={"providerId": serializers.IntegerField(min_value=0)}
        ),
        responses={
            201: OpenApiResponse(
                response=inline_serializer(
                    name="videoListSerializer",
                    fields={
                        "payment": {},
                        "providerId": serializers.IntegerField(min_value=0),
                        "applyDateTime": serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S"),
                    },
                ),
                description="모임원 신청 완료",
                examples=GROUP_APPLY_POST_EXAMPLE,
            )
        },
    )
    def apply_member(self, request, *args, **kwargs):
        """POST /groups/applies/member"""
        return self.apply(request, apply_type="M", *args, **kwargs)

    @extend_schema(
        tags=["Priority-1", "Group"],
        operation_id="모임장 신청",
        description="Apply leader of provider(id={provider_id})",
        request=inline_serializer(
            name="GroupApplyRequest", fields={"providerId": serializers.IntegerField(min_value=0)}
        ),
        responses={
            201: OpenApiResponse(
                response=inline_serializer(
                    name="videoListSerializer",
                    fields={
                        "payment": {},
                        "providerId": serializers.IntegerField(min_value=0),
                        "applyDateTime": serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S"),
                    },
                ),
                description="모임장 신청 완료",
                examples=GROUP_APPLY_POST_EXAMPLE,
            )
        },
    )
    def apply_leader(self, request, *args, **kwargs):
        """POST /groups/applies/leader"""
        return self.apply(request, apply_type="L", *args, **kwargs)

    @extend_schema(
        tags=["Priority-1", "Group"],
        operation_id="모임원 취소",
        description="Cancel applying of member",
        request=inline_serializer(
            name="GroupApplyRequest", fields={"providerId": serializers.IntegerField(min_value=0)}
        ),
        responses={
            200: OpenApiResponse(
                description="모임원 취소 완료",
            )
        },
    )
    def cancel_member(self, request, *args, **kwargs):
        """PUT /groups/applies/member"""
        try:
            _apply = self.get_object()
            _fellow_type = _apply.fellow_type
            _provider = _apply.provider
            # if user has payment information
            if hasattr(_apply, "payment") and _apply.payment is not None:
                _amount = _apply.payment.amount
            else:
                # user has spent mileages
                _amount = _provider.charge.service_charge_per_member
            # check fellow type with valid api
            if _apply.fellow_type != "M":
                raise ApplyFellowTypeNotMatchedException()
            # return mileages
            _refund_mileages = create_histories_and_update_mileages(request, _amount)
            # delete apply object
            self.perform_destroy(_apply)
            return Response(_refund_mileages, status=status.HTTP_200_OK)
        except Payment.DoesNotExist as payment_error:
            raise BadFormatException() from payment_error
        except Charge.DoesNotExist as charge_error:
            raise NotEnoughSubscriptionInformationException() from charge_error
        except SubscriptionType.DoesNotExist as subscription_error:
            raise NotEnoughSubscriptionInformationException() from subscription_error
        except Provider.DoesNotExist as provider_error:
            raise ProviderNotFoundException() from provider_error
        except ResultNotFoundException as not_found_error:
            raise ApplyNotFoundException() from not_found_error

    @extend_schema(
        tags=["Priority-1", "Group"],
        operation_id="모임장 취소",
        description="Cancel applying of leader",
        request=inline_serializer(
            name="GroupApplyRequest", fields={"providerId": serializers.IntegerField(min_value=0)}
        ),
        responses={
            204: OpenApiResponse(
                description="모임장 취소 완료",
            )
        },
    )
    def cancel_leader(self, request, *args, **kwargs):
        """PUT /groups/applies/leader"""
        try:
            _apply = self.get_object()
            # check fellow type with valid api
            if _apply.fellow_type != "L":
                raise ApplyFellowTypeNotMatchedException()
            # delete group apply object
            self.perform_destroy(_apply)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TypeError as type_error:
            raise BadFormatException() from type_error
        except KeyError as key_error:
            raise InvalidProviderIdException() from key_error
        except Provider.DoesNotExist as provider_error:
            raise ProviderNotFoundException() from provider_error
        except ResultNotFoundException as not_found_error:
            raise ApplyNotFoundException() from not_found_error
