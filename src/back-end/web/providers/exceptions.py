"""Exceptions related to providers application"""
from rest_framework import status
from rest_framework.exceptions import APIException


class SupportedProviderValidator(APIException):
    """exception if some provider is not supporting for using group service"""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "모임 서비스를 지원하지 않는 OTT입니다."
    default_code = "not_supported_validator"


class ProviderNotFoundException(APIException):
    """provider is not found"""

    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "존재하지 않는 OTT입니다."
    default_code = "not_found_provider"
