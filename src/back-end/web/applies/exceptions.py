"""Exceptions related to applies"""
from rest_framework.exceptions import APIException


class ApplyAlreadyExistException(APIException):
    """Apply conflicts"""

    status_code = 409
    default_detail = "이미 신청한 모임입니다."
    default_code = "group_conflicts"


class ApplyNotFoundException(APIException):
    """Apply conflicts"""

    status_code = 404
    default_detail = "모임 신청 기록을 찾을 수 없습니다."
    default_code = "apply_not_found"


class ApplyFellowTypeNotMatchedException(APIException):
    """Apply fellow type not matched"""

    status_code = 400
    default_detail = "모임 신청 타입이 올바르지 않습니다."
    default_code = "apply_type_not_matched"
