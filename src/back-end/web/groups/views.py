"""APIs of groups application"""

from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from mileages.models import Mileage
from payments.models import Payment
from providers.models import Provider
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response


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
        token = request.COOKIES.get('jwt')

        '''
        # request 값 확인
        # provider id로 가격 확인
        # user의 총 마일리지 확인
        # 총마일리지 값이 부족하지 않으면 그대로, 부족하면 error
        # 마일리지 내역 입력(mileages), 마일리지 감소 처리 최대한 동시에 하게 해주기
        # ㄴ> 이거랑 같이 payments 에도 기록 저장하기.
        # 전부 처리 된 다음에 response 날려줌.
        provider_id = request.POST["providerId"]  # request에서 provider_id 확인
        _amount = Provider.objects.get(Q(id=provider_id)).values("charge__service_charge_per_member")

        # 이제 유저의 마일리지 값 확인 -> 마일리지 값이 부족하지 않으면 그대로
        # 부족할시에 ERROR 처리를... 했다고 치고!
        mileage = Mileage(
            user=request.user,  # 대충 유저어케저케 확인해서 넣어주고
            ammout=_amount,
        )
        mileage.save()

        payment = Payment(
            amount=_amount,
            content="Mileage",
            category="N",
            method="V",
            status="D",
            approval_date_time=timezone.now,
        )
        payment.save()

        context = {
            "payment_id": payment.id,
            "amount": _amount,
            "request_date_time": timezone.now,
        }
        '''
        return Response(token, status=status.HTTP_201_CREATED)


class GroupApplyView(viewsets.ViewSet):
    """Class for member apply to Group"""

    MEMBER_MILEAGES = 1000  # 통일 처리

    @extend_schema()
    def list(self, request):
        """test"""
        return Response(status=status.HTTP_200_CREATED)
