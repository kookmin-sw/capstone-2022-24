"""Pagination classes to separate total video list"""
from config.exceptions.result import VideoHistoryNotFoundException
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class VideoHistoryPagination(LimitOffsetPagination):
    """Video pagenation used in mypage"""

    default_limit = 5
    limit_query_param = "videoLimit"
    offset_query_param = "videoOffset"

    def get_paginated_response(self, data):
        """Make paginated response with data"""
        try:
            if not data:
                raise VideoHistoryNotFoundException
            return Response(
                {
                    "page": {
                        "limit": self.limit,
                        "offset": self.offset,
                        "total_count": self.count,
                    },
                    "results": data,
                }
            )
        except VideoHistoryNotFoundException as video_not_found:
            raise VideoHistoryNotFoundException from video_not_found

    def get_paginated_result(self, data):
        """Make paginated result(not response!) with data"""
        return {
            "page": {
                "limit": self.limit,
                "offset": self.offset,
                "total_count": self.count,
            },
            "results": data,
        }
