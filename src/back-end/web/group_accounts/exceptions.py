"""Exceptions related to group_account"""
from rest_framework import status
from rest_framework.exceptions import APIException


class CanNotRegisterGroupAccountException(APIException):
    """can not register group acacount yet because of group status"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "아직 모임 계정을 등록할 수 없습니다."
    default_code = "invalid_group_status"
