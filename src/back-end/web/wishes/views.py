"""APIs of wishes application"""
from config.exceptions.input import (
    InvalidPaginationParameterException,
    InvalidVideoIdException,
)
from config.exceptions.result import ResultNotFoundException, VideoNotFoundException
from config.mixins import MultipleFieldLookupMixin
from drf_spectacular.utils import extend_schema, extend_schema_view
from mypages.pagination import VideoHistoryPagination
from rest_framework import permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response
from videos.models import Video
from wishes.exceptions import WishAlreadyExistsException, WishNotFoundException
from wishes.models import Wish
from wishes.schemas import WISH_LIST_EXAMPLES
from wishes.serializers import WishListSerializer, WishSerializer


# pylint: disable=R0901
@extend_schema(
    tags=["Priority-2", "User"],
    examples=WISH_LIST_EXAMPLES,
)
class WishListView(ListAPIView):
    """Wish apis of user's video history"""

    queryset = Wish.objects.select_related("user", "video")
    serializer_class = WishListSerializer
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

    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


@extend_schema_view(
    post=extend_schema(
        tags=["Priority-2", "User"],
        operation_id="찜 등록",
        description="Add wish list",
        request=None,
    ),
    delete=extend_schema(tags=["Priority-2", "User"], operation_id="찜 취소", description="Delete from wish list"),
)
class WishCreateAndDestroyView(MultipleFieldLookupMixin, CreateAPIView, DestroyAPIView):
    """[POST & DELETE] /videos/{video_id}/wishes/"""

    queryset = Wish.objects.all()
    serializer_class = WishSerializer
    permission_classes = [permissions.IsAuthenticated]  # TODO
    lookup_fields = ("user_id", "video_id")

    def get_valid_user_and_video(self, request, *args, **kwargs):
        """Validate user and video and return user, video dict"""
        try:
            video_id = kwargs["video_id"]
            user = self.request.user
            video = Video.objects.get(id=video_id)
        except KeyError as e:
            raise InvalidVideoIdException() from e
        except self.queryset.model.DoesNotExist as not_exist:
            raise VideoNotFoundException() from not_exist
        return {"user": user.id, "video": video.id}

    def create(self, request, *args, **kwargs):
        """Wish video"""
        try:
            data = self.get_valid_user_and_video(self, request, *args, **kwargs)
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as error:
            # error is from UniqueTogetherValidator
            error_codes = list(*error.get_codes().values())
            if "unique" in error_codes:
                raise WishAlreadyExistsException() from error
            # others
            raise error

    def destroy(self, request, *args, **kwargs):
        """Unwish video"""
        try:
            # set user id
            self.kwargs["user_id"] = request.user.id
            return super().destroy(self, request, *args, **kwargs)
        except ResultNotFoundException as not_found:
            raise WishNotFoundException() from not_found
