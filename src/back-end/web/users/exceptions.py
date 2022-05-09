"""Exception classes related to users application"""
from rest_framework.exceptions import ValidationError
from users.validators import match_status_code_with_nickname_validator_code


class NicknameValidationException(ValidationError):
    """Specify nickname validation exceptions"""

    status_code = 400
    default_detail = "닉네임을 사용할 수 없습니다."
    default_code = "invalid_nickname"

    def __init__(self, error):
        error_details = error.get_full_details().get("nickname")[0].get("message")
        detail = error_details.title()
        code = error_details.code
        if not detail:
            detail = self.default_detail
        if not code:
            code = self.default_code
        self.status_code = match_status_code_with_nickname_validator_code(code)
        super().__init__(detail, code)
