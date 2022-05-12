"""Exceptions List related to input value"""
from rest_framework.exceptions import APIException


class BadFormatException(APIException):
    """Custom Exception For wrong request format"""

    status_code = 400
    default_detail = "올바르지 않은 형식입니다."
    default_code = "Bad Request Key"
