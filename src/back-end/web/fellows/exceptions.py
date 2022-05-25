"""API exceptions related to fellows application"""
from rest_framework import status
from rest_framework.exceptions import APIException


class GroupFellowsCreationException(APIException):
    """Internal server error because of group matching"""

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "모임 구성원 정보를 구성할 수 없습니다."
    default_code = "internal_fellow_creation_error"
