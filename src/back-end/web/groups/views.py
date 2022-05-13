"""APIs of groups application"""

from datetime import datetime
from django.db.models import Q
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from rest_framework import permissions, serializers, status, viewsets
from rest_framework.response import Response

class GruopPayment(viewsets.ViewSet):
    """Class for member payments process to Group"""

    def payment(self, request):
        """re: asdifjalsjgkwaj"""


        request_date_time = datetime.now() 
        context= {
            "payment_id" : 0,
            "amount" : 0,
            "request_date_time" : request_date_time,
        }
        return Response(status=status.HTTP_201_CREATED)


class GroupApply(viewsets.ViewSet):
    """Class for member apply to Group"""
    MEMBER_MILEAGES = 1000 #통일 처리

    @extend_schema()
    def list() :
        return Response()
