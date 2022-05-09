"""Validator objects used in serializers"""
from django.core.validators import (
    BaseValidator,
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)
from rest_framework import status
from rest_framework.validators import UniqueValidator


class BaseValidatorWithCode(BaseValidator):
    """Custom validation class with code attribute"""

    code = "invalid_length"

    def __init__(self, validator, code=None):
        super().__init__(limit_value=validator.limit_value, message=validator.message)
        self.code = code or self.code
        # replace to validator's function
        self.compare = validator.compare
        self.clean = validator.clean


def get_nickname_validators():
    """Get validators related to set nickname"""
    return [
        BaseValidatorWithCode(
            validator=MinLengthValidator(
                1,
                message="닉네임은 1자 이상 입력해야 합니다.",
            ),
            code="invalid_min_length",
        ),
        BaseValidatorWithCode(
            validator=MaxLengthValidator(
                8,
                message="닉네임은 최대 8자까지 입력 가능합니다.",
            ),
            code="invalid_max_length",
        ),
        RegexValidator(regex=r"^[가-힣a-zA-Z0-9]+$", message="닉네임은 한글, 숫자, 영문자만 사용 가능합니다.", code="invalid_characters"),
    ]


def get_unique_nickname_validator(queryset):
    """Get unique validator that parameters are filled"""
    return UniqueValidator(
        queryset=queryset,
        message="이미 사용중인 닉네임입니다.",
    )


cell_phone_number_validator = RegexValidator(
    regex=r"^01\d-\d{3,4}-\d{4}$",
    message="핸드폰 번호는 01X-XXX-XXXX 혹은 01X-XXXX-XXXX 형식이어야 합니다.",
    code="invalid_cell_phone_number",
)


def match_status_code_with_nickname_validator_code(code):
    """get proper error status code with code attribute of validator"""
    status_code = status.HTTP_400_BAD_REQUEST
    if code:
        # invalid input -> BAD_REQUEST
        if code.startswith("invalid"):
            status_code = status.HTTP_400_BAD_REQUEST
        # duplicated -> CONFLICT
        elif code == "unique":
            status_code = status.HTTP_409_CONFLICT
    return status_code
