"""Exceptions List related to report"""
from rest_framework.exceptions import APIException


class GroupNotFoundExceptions(APIException):
    """Custom Exception that occurs when group is not exist"""

    status_code = 404
    default_detail = "모임이 존재하지 않습니다."
    default_code = "Group Not Exist"


class WrongFellowExceptions(APIException):
    """Custom Exception that occurs when a non-fellow user calls"""

    status_code = 403
    default_detail = "해당 모임에 속하지 않은 사용자입니다."
    default_code = "Wrong Fellow Id"


class WrongGroupStateExcetpions(APIException):
    """Custom Exception that occurs when group status is not suitable"""

    status_code = 412
    default_detail = "신고할 수 없는 상태의 모임입니다."
    default_code = "Wrong Group State"


class AlreadyReportExceptions(APIException):
    """Custom Exception that User has already reported"""

    status_code = 409
    default_detail = "이미 신고한 상태입니다."
    default_code = "Already reported"


class LeaderReportAuthorityExceptions(APIException):
    """Custom Exception that have None Authority to report"""

    status_code = 403
    default_detail = "해당 모임의 모임장에게 신고할 권한이 없습니다."
    default_code = "None Authority Report"


class NoneReportExceptions(APIException):
    """Custom Exception that Report Record is not found"""

    status_code = 404
    default_detail = "신고 기록이 없습니다."
    default_code = "Report not found"
