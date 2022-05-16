"""Pagination classes to separate total video list"""
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class VideoHistoryPagination(LimitOffsetPagination):
    """Video pagenation used in mypage"""

    default_limit = 5
    limit_query_param = "video_limit"
    offset_query_param = "video_offset"

    def get_paginated_response(self, data):
        """Make paginated response with data"""
        return Response(
            {
                "page": {
                    "limit": self.limit,
                    "offset": self.offset,
                    "total_count": self.count,
                },
                "count": self.count,
                "results": data,
            }
        )

    def get_paginated_result(self, data):
        """Make paginated result(not response!) with data"""
        return {
            "page": {
                "limit": self.limit,
                "offset": self.offset,
                "total_count": self.count,
            },
            "count": self.count,
            "results": data,
        }
