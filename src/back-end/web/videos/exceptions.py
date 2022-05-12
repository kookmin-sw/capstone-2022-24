"""Exceptions List to Use videos views"""
from rest_framework.exceptions import APIException


class WrongVideoIDException(APIException):
    """Custom Exception for wrong Video id"""

    status_code = 400
    default_detail = "작품 종류와 맞지않은 작품 ID입니다."
    default_code = "Bad Video ID"
