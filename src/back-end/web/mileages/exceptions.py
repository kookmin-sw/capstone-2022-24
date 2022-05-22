"""Exceptions about mileages"""
from rest_framework.exceptions import APIException


class MileageAmountException(APIException):
    """Amount exception of mileages"""

    status_code = 400
    default_detail = "마일리지 요청 값이 올바르지 않습니다."
    default_code = "invalid_mileage_amount"


class MinAmountValueException(APIException):
    """total_mileage must be positive or zero"""

    message = "총 마일리지 이하의 금액만 사용할 수 있습니다."
    code = "mileage_must_be_greater_than_zero"


class MaxAmountValueException(APIException):
    """total_mileage must be smaller than 2147483647"""

    message = "마일리지 요금 충전 한도를 초과했습니다."
    code = "out_of_range_amount"
