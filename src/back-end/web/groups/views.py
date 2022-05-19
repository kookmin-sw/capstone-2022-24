"""APIs of groups application"""
from config.exceptions.input import BadFormatException
from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import OpenApiResponse, extend_schema, inline_serializer
from groups.models import Group
from groups.serializers import GroupDetailSerializer, GroupPaymentResponseSerializer
from mileages.serializers import MileageSerializer
from payments.serializers import PaymentSaveSerializer
from providers.models import Charge
from rest_framework import serializers, status, viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from users.serializers import UserMileageSerializer


@extend_schema(
    tags=["Priority-1", "Group"],
    operation_id="모임원 결제",
    request=inline_serializer(
        name="GroupPaymentRequestSerializer",
        fields={"accessToken": serializers.CharField(), "providerId": serializers.IntegerField()},
    ),
    responses={201: OpenApiResponse(description="모임원 결제 성공", response=GroupPaymentResponseSerializer)},
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


class GroupDetailView(RetrieveAPIView):
    """GET /groups/{group_id}/"""

    queryset = Group.objects.select_related("provider", "group_account",).prefetch_related(
        "fellow_set",
        "fellow_set__user",
        "fellow_set__member",
        "fellow_set__leader",
    )
    serializer_class = GroupDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "group_id"
