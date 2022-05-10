"""Exceptions List related to result Value"""
from rest_framework.exceptions import APIException


class NoneResultException(APIException):
    """custom Search Exception for None Result"""

    status_code = 404
    default_detail = "존재하지 않은 결과값입니다."
    default_code = "None Result"


class NoneVideoException(APIException):
    """Custom Exception for None Video"""

    status_code = 404
    default_detail = "존재하지 않은 작품입니다."
    default_code = "None Video"
