"""APIs of groups application"""

from datetime import datetime

from applies.models import LeaderApply, MemberApply
from config.exceptions.input import BadFormatException
from django.db.models import Q
from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from mileages.models import Mileage
from payments.models import Payment
from providers.models import Charge, Provider
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response
from users.models import User


@extend_schema(
    tags=["Priority-1", "Group"],
    operation_id="모임 신청",
    request=inline_serializer(
        name="groupPaymentRequestSerializer",
        fields={"accessToken": serializers.CharField(), "providerId": serializers.IntegerField()},
    ),
    parameters=[
        OpenApiParameter(
            name="set-cookie ",
            description="ongot-token={{Access Token}}; expires=DAY, DD MON 2022 hh:mm:ss GMT; Max-Age=39600;",
            type=str,
            location="cookie",
            response=True,
        ),
        OpenApiParameter(
            name="set-cookie",
            description="ongot-refresh-token={{Refresh Token}}; expires=DAY, DD MON 2022 hh:mm:ss GMT; Max-Age=54000;",
            type=str,
            location="cookie",
            response=True,
        ),
    ],
    responses={
        201: OpenApiResponse(
            description="모임 결제 성공",
            response=inline_serializer(
                name="GruopPaymentSerializer",
                fields={
                    "paymentId": serializers.IntegerField(),
                    "amount": serializers.IntegerField(),
                    "requestDateTime": serializers.DateField(),
                },
            ),
        )
    },
)
class GruopPaymentView(viewsets.ViewSet):
    """Class for member payments process to Group"""

    def payment(self, request):
        """method: get to payment 처리"""
        _user = request.user
        provider_id = request.data["provider_id"]

        try:
            _amount = Charge.objects.get(Q(provider=provider_id)).service_charge_per_member
        except Charge.DoesNotExist as e:
            raise BadFormatException() from e

        if _amount > _user.total_mileages:
            raise BadFormatException()

        mileage = Mileage(
            user=_user,
            amount=_amount,
        )
        payment = Payment(
            amount=_amount,
            content="Mileage",
            category="N",
            method="V",
            status="D",
            approval_date_time=datetime.now(),
        )
        mileage.save()
        payment.save()

        context = {
            "payment_id": payment.id,
            "amount": _amount,
            "request_date_time": datetime.now(),
        }
        return Response(context, status=status.HTTP_201_CREATED)


class GroupApplyView(viewsets.ViewSet):
    """Class for member apply to Group"""

    MEMBER_MILEAGES = 1000  # 통일 처리

    @extend_schema()
    def apply_member(self, request):
        """test"""
        _user = request.user
        provider_id = request.data["provider_id"]
        payment_id = request.data["payment_id"]

        member_apply = MemberApply(
            user=_user,
            payment=Payment.objects.get(Q(id=payment_id)),
            provider=Provider.objects.get(Q(id=provider_id)),
            apply_date_time=datetime.now(),
        )
        member_apply.save()

        context = {"member_apply_id": member_apply.id}

        return Response(context, status=status.HTTP_201_CREATED)

    def apply_leader(self, request):
        """test"""
        _user = request.user
        provider_id = request.data["provider_id"]

        leader_apply = LeaderApply(
            user=_user, provider=Provider.objects.get(Q(id=provider_id)), apply_date_time=datetime.now()
        )
        leader_apply.save()

        context = {"leader_apply_id": leader_apply.id}

        return Response(context, status=status.HTTP_201_CREATED)

    def cancel_member(self, request, key=None):
        """test"""
        _user = request.user
        member_apply_id = request.data["member_apply_id"]
        # cancel = request.data["cancel"]

        member_apply = MemberApply.objects.get(Q(id=member_apply_id))
        _amount = member_apply.payment.amount
        provider_id = member_apply.provider.id
        payment = Payment(
            amount=_amount,
            content="Mileage",
            category="N",
            method="V",
            status="C",
            approval_date_time=datetime.now(),
        )
        mileage = Mileage(
            user=_user,
            amount=_amount * (-1),
        )

        payment.save()
        mileage.save()
        member_apply.delete()

        User.objects.filter(id=_user.id).update(total_mileages=_user.total_mileages + _amount)

        context = {"user_id": _user.id, "payment_id": payment.id, "provider_id": provider_id}
        return Response(context, status=status.HTTP_200_OK)

    def cancel_leader(self, request):
        """test"""
        _user = request.user
        leader_apply_id = request.data["leader_apply_id"]
        # cancel = request.data["cancel"]

        leader_apply = MemberApply.objects.get(Q(id=leader_apply_id))
        provider_id = leader_apply.provider.id

        leader_apply.delete()

        context = {"user_id": _user.id, "provider_id": provider_id}
        return Response(context, status=status.HTTP_200_OK)
