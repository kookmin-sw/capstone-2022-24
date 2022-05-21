"""Exceptions List related to result Value"""
from rest_framework.exceptions import APIException


class ResultNotFoundException(APIException):
    """Custom Search Exception for None Result"""

    status_code = 404
    default_detail = "존재하지 않은 결과값입니다."
    default_code = "None Result"


class VideoNotFoundException(APIException):
    """Custom Exception for None Video"""

    status_code = 404
    default_detail = "존재하지 않은 작품입니다."
    default_code = "None Video"


class VideoHistoryNotFoundException(APIException):
    """Custom Exception for None Video"""

    status_code = 404
    default_detail = "작품 기록이 존재하지 않습니다."
    default_code = "not_found_video_histories"
