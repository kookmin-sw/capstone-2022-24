"""APIs of mileage application"""
from config.exceptions.input import BadFormatException
from drf_spectacular.utils import extend_schema, extend_schema_view
from mileages.serializers import MileageSerializer
from rest_framework import viewsets
from rest_framework.response import Response


# pylint: disable=R0901
@extend_schema_view(
    operation_id="마일리지",
    get=extend_schema(tags=["Priority-1", "User"], operation_id="마일리지 내역 조히", description="Get mileage histories"),
    post=extend_schema(tags=["Priority-3", "User"], operation_id="마일리지 충전", description="Charge milages"),
    patch=extend_schema(tags=["Priority-1", "User"], operation_id="마일리지 사용", description="Use milages"),
)
class MileageViewSet(viewsets.ModelViewSet):
    """Mileage API: GET/PUT/PATCH /mileages/"""

    serializer_class = MileageSerializer
    http_method_names = [
        "get",
        "post",
        "patch",
    ]

    def get_queryset(self):
        return self.request.user.mileage_set.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        serializer = self.get_serializer(data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.perform_create()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        try:
            kwargs["partial"] = True
            # amount is not numb현er
            if not isinstance(kwargs["amount"], int):
                raise ValueError
            # change positive/negative value
            kwargs["amount"] = -kwargs["amount"]
            return self.update(request, *args, **kwargs)
        except KeyError as e:
            raise BadFormatException from e
        except ValueError as e:
            raise BadFormatException from e
