"""Exception classes related to watching mark apis"""
from rest_framework.exceptions import APIException


class WatchingMarkNotFoundException(APIException):
    """Custom Search Exception for None Result"""

    status_code = 404
    default_detail = "관람 표시한 기록을 찾을 수 없습니다."
    default_code = "Watching Mark not found"


class WatchingMarkAlreadyExistsException(APIException):
    """Wish already Exists when someone tries to create"""

    status_code = 409
    default_detail = "이미 관람표시한 작품입니다."
    default_code = "Watching Mark conflicts"
