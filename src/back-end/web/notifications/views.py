"""APIs of notifications application"""
from drf_spectacular.utils import extend_schema, extend_schema_view
from notifications.models import Notification
from notifications.paginations import NotificationPagination
from notifications.serializers import NotificationSerializer
from rest_framework.generics import ListAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response


@extend_schema_view(
    operation_id="알림",
    list=extend_schema(
        tags=["Priority-3", "User"],
        operation_id="알림 목록 조회",
        description="Get notification list (limit=?, offset=?)",
    ),
    partial_update=extend_schema(
        tags=["Priority-3", "User"],
        operation_id="알림 전체 읽음 표시",
        description="Read all notifications",
    ),
)
class NotificationListAndUpdateView(UpdateModelMixin, ListAPIView):
    """Notification whole list or read update view"""

    serializer_class = NotificationSerializer
    queryset = Notification.objects.select_related(
        "user",
        "provider",
        "content",
    )
    pagination_class = NotificationPagination
    http_method_names = ("get", "patch")

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.id)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        _user = request.user
        _notifications = self.get_queryset()
        _read_marked_notifications_id = []
        for notification in _notifications:
            serializer = self.get_serializer(notification, {"has_read": True}, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            _read_marked_notifications_id.append(notification.id)
        return Response(_read_marked_notifications_id)
