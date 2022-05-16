"""APIs of wishes application"""
from config.exceptions.input import InvalidPaginationParameterException
from mypages.pagination import VideoHistoryPagination
from rest_framework import viewsets
from wishes.models import Wish
from wishes.serializers import WishSerializer


# pylint: disable=R0901
class WishViewSet(viewsets.ModelViewSet):
    """Wish apis of user's video history"""

    queryset = Wish.objects.select_related("user", "video")
    serializer_class = WishSerializer
    pagination_class = VideoHistoryPagination

    def get_queryset(self):
        """get login user's wish objects"""
        # (required) query parameters: videoLimit & videoOffset (used in pagination)
        if VideoHistoryPagination.limit_query_param not in self.request.query_params:
            raise InvalidPaginationParameterException()
        if VideoHistoryPagination.offset_query_param not in self.request.query_params:
            raise InvalidPaginationParameterException()
        # other query parameters are included
        if len(self.request.query_params) >= 3:
            raise InvalidPaginationParameterException()
        return self.request.user.wish_set.all()
