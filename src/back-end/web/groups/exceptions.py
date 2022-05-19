"""Exception classes of groups application"""
from rest_framework.exceptions import APIException


class GroupNotFoundException(APIException):
    """404 group Not found"""

    status_code = 404
    default_detail = "존재하지 않는 모임입니다."
    default_code = "group_not_found"


class WatchingDurationException(APIException):
    """400 group watching time invalid"""

    status_code = 400
    default_detail = "모임의 관람 기간이 올바르지 않습니다."
    default_code = "invallid_watching_duration"
