"""APIs of providers application"""
from django.db.models import Q
from drf_spectacular.utils import extend_schema
from providers.models import Provider
from providers.serializers import ProviderListByApplyTypeSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from users.models import User


def get_providers_by_user_apply_type(user: User):
    """make each provider list using queryset"""
    _queryset = Provider.objects.prefetch_related(
        "memberapply_set",
        "memberapply_set__user",
        "leaderapply_set",
        "leaderapply_set__user",
        "group_set",
        "group_set__fellow_set",
        "group_set__fellow_set__user",
    )  # type: QuerySet[Provider]

    # get applied providers
    _filter = Q(memberapply__user=user) | Q(leaderapply__user=user) | Q(group__fellow__user=user)
    _applied_providers = _queryset.filter(_filter).all()  # type: QuerySet[Provider]

    # get not-applied providers
    _not_applied_providers = _queryset.exclude(id__in=_applied_providers).all()
    # make dictionary data
    providers = dict(
        applied_providers=list(_applied_providers),
        not_applied_providers=list(_not_applied_providers),
    )
    return providers


@extend_schema(tags=["Priority-1", "Group"], operation_id="모임 신청 여부별 OTT 목록 조회")
class ProviderListByApplyTypeView(GenericAPIView):
    """Provider list by apply types"""

    queryset = None
    serializer_class = ProviderListByApplyTypeSerializer

    def get_queryset(self):
        """Get providers in two categories"""
        return get_providers_by_user_apply_type(self.request.user)

    def get(self, request, *args, **kwargs):
        """Get providers"""
        _provider = self.get_queryset()
        serializer = self.get_serializer(_provider)
        return Response(serializer.data)
