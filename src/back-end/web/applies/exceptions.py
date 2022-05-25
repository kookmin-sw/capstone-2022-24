"""Exceptions related to applies"""
from rest_framework import status
from rest_framework.exceptions import APIException


class ApplyAlreadyExistException(APIException):
    """Apply conflicts"""

    status_code = status.HTTP_409_CONFLICT
    default_detail = "이미 신청한 모임입니다."
    default_code = "group_conflicts"
