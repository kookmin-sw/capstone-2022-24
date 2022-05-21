"""Exceptions about mileages"""
from rest_framework.exceptions import APIException


class MileageAmountException(APIException):
    """Amount exception of mileages"""

    status_code = 400
    default_detail = "마일리지 요청 값이 올바르지 않습니다."
    default_code = "invalid_mileage_amount"
