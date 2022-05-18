"""Exception classes of groups application"""
from rest_framework.exceptions import APIException


class GroupNotFoundException(APIException):
    """404 group Not found"""

    status_code = 404
    default_detail = "존재하지 않는 모임입니다."
    default_code = "group_not_found"
