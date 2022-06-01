"""Pagination classes to notifications list"""
from notifications.exceptions import NotificationNotFoundException
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class NotificationPagination(LimitOffsetPagination):
    """Video pagenation used in mypage"""

    default_limit = 5
    limit_query_param = "limit"
    offset_query_param = "offset"

    def get_paginated_response(self, data):
        """Make paginated response with data"""
        try:
            if not data:
                raise NotificationNotFoundException
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
        except NotificationNotFoundException as video_not_found:
            raise NotificationNotFoundException from video_not_found

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

    def get_paginated_response_schema(self, schema):
        """Get paginated schema used in spectacular"""
        return {
            "page": {
                "limit": "integer",
                "offset": "integer",
                "total_count": "integer",
            },
            "results": schema,
        }
