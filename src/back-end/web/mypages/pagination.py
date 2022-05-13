"""Pagination classes to separate total video list"""
from rest_framework.pagination import LimitOffsetPagination


class MyVideoPagination(LimitOffsetPagination):
    """Video pagenation used in mypage"""

    default_limit = 24
