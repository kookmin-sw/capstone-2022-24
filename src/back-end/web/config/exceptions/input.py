"""Exceptions List related to input value"""
from rest_framework.exceptions import APIException


class BadFormatException(APIException):
    """Custom Exception For wrong request format"""

    status_code = 400
    default_detail = "올바르지 않은 형식입니다."
    default_code = "Bad Request Key"


class InvalidPaginationParameterException(APIException):
    """Query parameter(s) related to pagination is(are) not allowed or required query parameter(s) is(are) missing"""

    status_code = 400
    default_detail = "페이지 요청 형식이 올바르지 않습니다."
    default_code = "invalid Pagination"
