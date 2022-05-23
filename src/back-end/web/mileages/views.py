"""APIs of mileage application"""
from config.exceptions.input import BadFormatException
from drf_spectacular.utils import extend_schema, extend_schema_view
from mileages.exceptions import MileageAmountException
from mileages.models import Mileage
from mileages.schemas import (
    MILEAGE_PARTIAL_UPDATE_EXAMPLES,
    MILEAGE_POST_EXAMPLES,
    MILEAGES_LIST_EXAMPLES,
)
from mileages.serializers import MileageSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response


# pylint: disable=R0901
@extend_schema_view(
    operation_id="마일리지",
    list=extend_schema(
        tags=["Priority-1", "User"],
        operation_id="마일리지 내역 조회",
        description="Get mileage histories",
        examples=MILEAGES_LIST_EXAMPLES,
    ),
    create=extend_schema(
        tags=["Priority-3", "User"],
        operation_id="마일리지 충전",
        description="Charge milages",
        examples=MILEAGE_POST_EXAMPLES,
    ),
    partial_update=extend_schema(
        tags=["Priority-1", "User"],
        operation_id="마일리지 사용",
        description="Use milages",
        examples=MILEAGE_PARTIAL_UPDATE_EXAMPLES,
    ),
)
class MileageViewSet(viewsets.ModelViewSet):
    """Mileage API: GET/PUT/PATCH /mileages/"""

    queryset = Mileage.objects.select_related("user").all()
    serializer_class = MileageSerializer
    http_method_names = [
        "get",
        "post",
        "patch",
    ]

    def get_queryset(self):
        """Get mileage histories"""
        return self.request.user.mileage_set.all()

    def create_history(self, request):
        """Create mileage history with serializer"""
        try:
            serializer = self.get_serializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return serializer.data
        except ValueError as value_error:
            raise MileageAmountException from value_error

    def create(self, request, *args, **kwargs):
        """POST /mileages/"""
        _history = self.create_history(request)
        headers = self.get_success_headers(_history)
        return Response(_history, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        """PATCH /mileages/"""
        try:
            # change positive/negative value
            if request.data and request.data.get("amount"):
                request.data["amount"] *= -1
            _history = self.create_history(request)
            return Response(_history)
        except ValueError as e:
            raise BadFormatException from e


def create_histories_and_update_mileages(request, amount):
    """update user's mileage and create mileage history"""
    serializer = MileageSerializer(data={"amount": amount}, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data
