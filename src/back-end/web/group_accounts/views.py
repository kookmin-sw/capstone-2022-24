"""APIs of group_accounts application"""
from drf_spectacular.utils import extend_schema, extend_schema_view
from group_accounts.exceptions import CanNotRegisterGroupAccountException
from group_accounts.models import GroupAccount
from group_accounts.serializers import (
    GroupAccountIDSerializer,
    GroupAccountPWSerializer,
)
from groups.models import Group
from groups.views import can_start_watch, start_watch
from rest_framework.exceptions import ValidationError
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated


class GroupAccountView(UpdateAPIView):
    """Base group account id/pw view"""

    queryset = GroupAccount.objects.prefetch_related(
        "group", "group__provider", "group__fellow_set", "group__fellow_set__user", "group__fellow_set__leader"
    )  # type: QueryDict[GroupAccount]
    permission_classes = (IsAuthenticated,)  # TODO: IsLeaderOrFellowReadOnly
    lookup_field = "group__id"
    lookup_url_kwarg = "group_id"
    http_method_names = ["patch"]

    def patch(self, request, *args, **kwargs):
        """PATCH /groups/{group_id}/account/id"""
        try:
            _account = self.get_object()  # type: GroupAccount
            _group = _account.group
            # 모임의 계정 변경 가능 여부 확인
            # (1. 리더 여부 & 권한 확인 - permission_classes에서 확인)
            # 2. 모임 상태 확인: 모집 완료 맞음?
            if not _group.can_register_account:
                raise CanNotRegisterGroupAccountException
            # 모임 계정 변경
            response = super().patch(request, *args, **kwargs)
            # 저장 후 새로 fetch
            # + 모임 상태 변경 필요? (모집완료 -> 관람중~)
            _q = Group.objects.select_related("group_account")
            _patched_group = _q.get(id=kwargs.get("group_id"))
            if can_start_watch(_patched_group):
                # 모임 상태 변경
                start_watch(_group, _q)
            return response
        except ValidationError as error:
            raise error


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
