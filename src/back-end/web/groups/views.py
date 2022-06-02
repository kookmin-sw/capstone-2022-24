"""APIs of groups application"""
from applies.models import GroupApply
from applies.serializers import ApplyDetailSerializer
from config.exceptions.input import BadFormatException
from config.exceptions.result import ResultNotFoundException
from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiResponse, extend_schema, inline_serializer
from group_accounts.models import GroupAccount
from groups.exceptions import GroupNotFoundException, WatchingDurationException
from groups.models import Group
from groups.schemas import GROUP_PAYMENT_EXAMPLES
from groups.serializers import GroupDetailSerializer, GroupPaymentResponseSerializer
from mileages.serializers import MileageSerializer
from payments.serializers import PaymentSaveSerializer
from providers.exceptions import ProviderNotFoundException
from providers.models import Charge, Provider, SubscriptionType
from rest_framework import serializers, status, viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from users.serializers import UserMileageSerializer


@extend_schema(
    tags=["Deprecated"],
    operation_id="모임원 결제",
    request=inline_serializer(
        name="GroupPaymentRequestSerializer",
        fields={"providerId": serializers.IntegerField()},
    ),
    responses={
        201: OpenApiResponse(
            description="모임원 결제 성공",
            response=inline_serializer(
                name="GroupPaymentSerializerSample",
                fields={
                    "paymentId": serializers.IntegerField(),
                    "amount": serializers.IntegerField(),
                    "requestDateTime": serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S"),
                },
            ),
            examples=GROUP_PAYMENT_EXAMPLES,
        )
    },
)
class GruopPaymentView(viewsets.ViewSet):
    """Class for member payments process to Group"""

    def payment(self, request):
        """Method: process payments for Member to apply Group"""

        _user = request.user
        provider_id = request.data["provider_id"]

        try:
            _amount = Charge.objects.get(Q(provider=provider_id)).service_charge_per_member
        except Charge.DoesNotExist as e:
            raise BadFormatException() from e

        user_serializer = UserMileageSerializer(_user, data={"total_mileages": _user.total_mileages - _amount})

        if not user_serializer.is_valid():
            raise BadFormatException()
            # 이부분은 금액 부족으로 따로 exceptions 처리 바꿔도 될거 같음

        mileage_serializer = MileageSerializer(data={"amount": _amount, "renewal_date_time": timezone.now()})
        payment_serializer = PaymentSaveSerializer(
            data={
                "amount": _amount,
                "content": "Mileage",
                "category": "N",
                "method": "V",
                "status": "D",
                "approval_date_time": timezone.now(),
            }
        )

        if mileage_serializer.is_valid(raise_exception=True) & payment_serializer.is_valid(raise_exception=True):
            mileage_serializer.save(user=_user)
            payment_serializer.save()
            user_serializer.save()

        response_serializer = GroupPaymentResponseSerializer(
            data={"payment_id": payment_serializer.data["id"], "amount": _amount, "request_date_time": timezone.now()}
        )
        response_serializer.is_valid(raise_exception=True)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


@extend_schema(tags=["Priority-1", "Group"], operation_id="모임 상세 조회")
class GroupDetailView(RetrieveAPIView):
    """GET /groups/{group_id}/"""

    queryset = Group.objects.select_related("provider", "group_account",).prefetch_related(
        "fellow_set",
        "fellow_set__user",
        "fellow_set__member",
        "fellow_set__leader",
    )
    serializer_class = GroupDetailSerializer
    lookup_field = "provider_id"
    lookup_url_kwarg = "provider_id"

    def get_apply(self, *args, **filter_kwargs):
        """GET apply object of leader or member"""
        _apply_queryset = GroupApply.objects.select_related("provider", "user")
        _user = self.request.user
        try:
            filter_kwargs["user_id"] = _user.id
            _apply = _apply_queryset.get(**filter_kwargs)
            return _apply
        except GroupApply.DoesNotExist as apply_error:
            raise GroupNotFoundException from apply_error

    def get_object(self):
        """Return group or apply object if user is related to provider(id={provider_id}) else 404 error"""
        # find group by lookup field and path parameter
        _queryset = self.get_queryset()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        _filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            _filter = _filter_kwargs.copy()
            _filter["fellow__user_id"] = self.request.user.id
            _group = _queryset.get(**_filter)
            self.check_object_permissions(self.request, _group)
            return _group
        except _queryset.model.DoesNotExist:
            # applied group but not joined yet
            _apply = self.get_apply(**_filter_kwargs)
            return _apply

    def get_serializer(self, *args, **kwargs):
        """Return the serializer instance"""
        serializer_class = self.get_serializer_class()
        if args:
            # not group but apply -> ApplyDetailSerializer
            if args[0].__class__ is GroupApply:
                serializer_class = ApplyDetailSerializer
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)


def delete_expired_group(group: Group):
    """Delete group when watching time is passed"""
    if group.end_watching_date_time < timezone.now():
        group.delete()


def start_watch(group: Group, queryset=Group.objects):
    """set start / end watching time of group"""
    try:
        _queryset = queryset.select_related("provider").prefetch_related(
            "provider__charge", "provider__charge__subscription_type"
        )
        # start: datetime at group_account created
        start_date_time = timezone.now()
        # end: datetime at start_time + subscription duration
        _subscription_detail = group.provider.charge.subscription_type
        end_date_time = start_date_time + _subscription_detail.duration
        # set watching duration
        group.start_watching_with_duration(start_date_time, end_date_time)
    except Provider.DoesNotExist as provider_error:
        raise ResultNotFoundException from provider_error  # TODO: 예외 구체화 필요
    except Charge.DoesNotExist as charge_error:
        raise ResultNotFoundException from charge_error  # TODO: 예외 구체화 필요
    except SubscriptionType.DoesNotExist as subscription_error:
        raise ResultNotFoundException from subscription_error  # TODO: 예외 구체화 필요
    except WatchingDurationException as duration_error:
        raise duration_error


def can_start_watch(group: Group):
    """can not watch before, but can watch now"""
    try:
        # check group does not start watching yet
        _recruited = group.is_waiting_for_watching
        # check account is fulfilled and valid
        _registered = group.group_account.has_registered and group.group_account.can_watch
        return _recruited and _registered
    except Group.DoesNotExist as g:
        raise GroupNotFoundException from g
    except GroupAccount.DoesNotExist as ga:
        raise GroupNotFoundException from ga


def create_group_with_provider(provider: Provider):
    """Create group object and returns it"""
    try:
        _group = Group.objects.create(provider=provider)
        return _group
    except Provider.DoesNotExist as e:
        raise ProviderNotFoundException() from e
