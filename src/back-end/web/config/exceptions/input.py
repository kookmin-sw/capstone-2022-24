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


class InvalidVideoIdException(APIException):
    """Invalid video_id path parameter"""

    status_code = 400
    default_detail = "작품 ID가 올바르지 않습니다."
    default_code = "invalid Video ID"


class UnknownRequestException(APIException):
    """Invalid video_id path parameter"""

    status_code = 400
    default_detail = "올바르지 않은 요청입니다."
    default_code = "invalid_request"


class InvalidProviderIdException(APIException):
    """Invalid provider in request data"""

    status_code = 400
    default_detail = "OTT 정보가 올바르지 않습니다."
    default_code = "invalid_provider"


class NotSupportedProviderException(APIException):
    """Not supported provider in applying group"""

    status_code = 400
    default_detail = "모임을 지원하지 않는 OTT입니다."
    default_code = "not_supported_provider"


class AlreadyJoinedGroupException(APIException):
    """User already joined group of provider"""

    status_code = 409
    default_detail = "이미 모임에 가입한 OTT입니다."
    default_code = "already_joined_provider_group"


class NotEnoughSubscriptionInformationException(APIException):
    """Not enough subscription_type, charge information about the provider (actually 500 error)"""

    status_code = 404
    default_detail = "모임 요금 정보를 찾을 수 없습니다."
    default_code = "not_found_subscription_information"
