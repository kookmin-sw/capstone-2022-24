"""Pagination classes to separate total video list"""
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class VideoHistoryPagination(LimitOffsetPagination):
    """Video pagenation used in mypage"""

    default_limit = 24
    limit_query_param = "limit"
    offset_query_param = "offset"

    def get_paginated_response(self, data):
        """Make paginated response with data"""
        return Response(
            {
                "page": {
                    "limit": self.page.paginator.limit,
                    "offset": self.page.paginator.offset,
                    "total_count": self.page.paginator.count,
                },
                "count": self.page.paginator.count,
                "results": data,
            }
        )

    def get_paginated_result(self, data):
        """Make paginated result(not response!) with data"""
        return {
            "page": {
                "limit": self.page.paginator.limit,
                "offset": self.page.paginator.offset,
                "total_count": self.page.paginator.count,
            },
            "count": self.page.paginator.count,
            "results": data,
        }
