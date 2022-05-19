"""APIs of group_accounts application"""
from drf_spectacular.utils import extend_schema, extend_schema_view
from group_accounts.models import GroupAccount
from group_accounts.serializers import (
    GroupAccountIDSerializer,
    GroupAccountPWSerializer,
)
from groups.models import Group
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated


class GroupAccountView(UpdateAPIView):
    """Base group account id/pw view"""

    queryset = GroupAccount.objects.prefetch_related(
        "group", "group__provider" "group__fellow_set", "group__fellow_set__user", "group__fellow_set__leader"
    )  # type: QueryDict[Group]
    permission_classes = (IsAuthenticated,)  # TODO: IsLeaderOrFellowReadOnly
    lookup_field = "group__id"
    lookup_url_kwarg = "group_id"
    http_method_names = ["patch"]


@extend_schema_view(
    operation_id="OTT 계정 ID 변경",
    patch=extend_schema(
        tags=["Priority-1", "Group"],
        operation_id="OTT 계정 ID 변경",
        description="Set identifier of the group account by leader",
    ),
)
class GroupAccountIDView(GroupAccountView):
    """PATCH /groups/{group_id}/accounts/id: Set Group Account ID"""

    serializer_class = GroupAccountIDSerializer


@extend_schema_view(
    operation_id="OTT 계정 PW 변경",
    patch=extend_schema(
        tags=["Priority-1", "Group"], operation_id="OTT 계정 PW 변경", description="Set password of the group account"
    ),
)
class GroupAccountPWView(GroupAccountView):
    """PATCH /groups/{group_id}/accounts/password: Set Group Account PW"""

    serializer_class = GroupAccountPWSerializer
