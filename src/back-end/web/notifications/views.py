"""APIs of notifications application"""
from config.exceptions.input import (
    BadFormatException,
    InvalidPaginationParameterException,
)
from django.db.models import Q
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from notifications.exceptions import NotificationNotFoundException
from notifications.models import Notification, NotificationContent
from notifications.paginations import NotificationPagination
from notifications.schemas import NOTIFICATION_LIST_EXAMPLES
from notifications.serializers import NotificationSerializer
from providers.exceptions import NotFoundProviderException
from providers.models import Provider
from rest_framework.generics import ListAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response


@extend_schema_view(
    operation_id="알림",
    get=extend_schema(
        tags=["Priority-3", "User"],
        operation_id="알림 목록 조회",
        parameters=[
            OpenApiParameter(
                name="read",
                description="hasRead options (Y/N/all)",
                type=str,
            )
        ],
        description="Get notification list (limit=?, offset=?, read=Y/N/all)",
        examples=NOTIFICATION_LIST_EXAMPLES,
    ),
    patch=extend_schema(
        tags=["Priority-3", "Deprecated"],
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

    def get_queryset(self, *args, **kwargs):
        """Get notifications queryset"""
        try:
            _filter = Q(user_id=self.request.user.id)
            _params = self.request.query_params
            # validate pagination parameters
            if "limit" in _params:
                int(_params.get("limit"))
            if "offset" in _params:
                int(_params["offset"])
            # validate read parameter
            if "read" in _params:
                if _params["read"] in ("Y", "N"):
                    has_read = _params["read"] == "Y"
                    _filter &= Q(has_read=has_read)
                elif _params["read"] != "all":
                    raise BadFormatException()
            # validate other parameter
            if set(filter(lambda x: x not in ("limit", "offset", "read"), _params.keys())):
                raise BadFormatException()
            # filter queryset
            _queryset = self.queryset.filter(_filter).all()
            # if queryset is empty
            if not _queryset:
                raise Notification.DoesNotExist
            # queryset exists
            return _queryset
        except ValueError as type_error:
            raise InvalidPaginationParameterException from type_error
        except Notification.DoesNotExist as not_exist:
            raise NotificationNotFoundException from not_exist

    def update(self, request, *args, **kwargs):
        """Read mark one's all notifications"""
        try:
            partial = kwargs.pop("partial", False)
            if hasattr(self.request.query_params, "read"):
                raise BadFormatException()
            _notifications = self.get_queryset()
            _read_marked_notifications_id = []
            for notification in _notifications:
                serializer = self.get_serializer(notification, {"has_read": True}, partial=partial)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                _read_marked_notifications_id.append(notification.id)
            return Response(_read_marked_notifications_id)
        except Notification.DoesNotExist as notification_not_exist:
            raise NotificationNotFoundException from notification_not_exist
        except Provider.DoesNotExist as provider_not_exist:
            raise NotFoundProviderException from provider_not_exist
        except NotificationContent.DoesNotExist as notification_content_not_exist:
            raise NotificationNotFoundException from notification_content_not_exist

    def read_all_notifications(self, user_id):
        """For async working"""
        _filter = Q(user_id=user_id) & Q(has_read=False)
        _queryset = self.queryset.filter(_filter).all()
        _read_marked_notifications = []
        for notification in _queryset:
            notification.has_read = True  # read mark!
            notification.save()
            _read_marked_notifications.append(notification.id)
        return _read_marked_notifications
