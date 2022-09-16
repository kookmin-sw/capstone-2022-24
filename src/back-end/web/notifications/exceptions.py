"""Exceptions related to notifications application"""
from rest_framework.exceptions import APIException


class NotificationNotFoundException(APIException):
    """Notification not exists"""

    status_code = 404
    default_code = "notification_not_found"
    default_detail = "알림이 존재하지 않습니다."
