"""Exception classes related to wish apis"""
from rest_framework.exceptions import APIException


class WishNotFoundException(APIException):
    """Custom Search Exception for None Result"""

    status_code = 404
    default_detail = "찜한 기록을 찾을 수 없습니다."
    default_code = "Wish not found"


class WishAlreadyExistsException(APIException):
    """Wish already Exists when someone tries to create"""

    status_code = 409
    default_detail = "이미 찜한 작품입니다."
    default_code = "Wish conflicts"
