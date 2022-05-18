"""APIs of group_accounts application"""
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
    permission_classes = [IsAuthenticated]  # TODO: IsLeaderOrFellowReadOnly
    lookup_field = "group__id"
    lookup_url_kwarg = "group_id"


class GroupAccountIDView(GroupAccountView):
    """PATCH /groups/{group_id}/accounts/id: Set Group Account ID"""

    serializer_class = GroupAccountIDSerializer


class GroupAccountPWView(GroupAccountView):
    """PATCH /groups/{group_id}/accounts/password: Set Group Account PW"""

    serializer_class = GroupAccountPWSerializer
