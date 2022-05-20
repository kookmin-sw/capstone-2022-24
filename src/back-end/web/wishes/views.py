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
from users.models import User
from videos.models import Video
from wishes.exceptions import WishAlreadyExistsException, WishNotFoundException
from wishes.schemas import WISH_LIST_EXAMPLES
from wishes.serializers import WishListSerializer, WishSerializer


# pylint: disable=R0901
@extend_schema(
    tags=["Priority-2", "User"],
    examples=WISH_LIST_EXAMPLES,
)
class WishListView(ListAPIView):
    """Wish apis of user's video history"""

    queryset = User.objects.prefetch_related("wish_set", "wish_set__user" "wish_set__video")
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

    queryset = Video.objects.prefetch_related("wish_set", "wish_set__user", "videototalcount")
    serializer_class = WishSerializer
    permission_classes = (permissions.IsAuthenticated,)  # TODO
    lookup_fields = ("user", "video")

    def get_video_by_id(self, video_id):
        """Find video object among queryset by its id"""
        try:
            _queryset = self.queryset
            _video = _queryset.get(id=video_id)
            return _video
        except Video.objects.model.DoesNotExist as not_exist:
            raise VideoNotFoundException() from not_exist

    def get_queryset(self):
        """Get wish queryset belongs to video object"""
        _id = self.kwargs.get("video_id", None)
        _video = self.get_video_by_id(_id) if _id else None  # type: Video
        return _video.wish_set

    def get_video_from_request(self, request, *args, **kwargs):
        """Validate user and video and return user, video dict"""
        try:
            _video_id = kwargs["video_id"]
            _video = self.get_video_by_id(_video_id)
        except KeyError as e:
            raise InvalidVideoIdException() from e
        return _video

    def get_wish_fk(self, user, video):
        """Get wish request detail with user, video ids"""
        return {"user": user.id, "video": video.id}

    def create(self, request, *args, **kwargs):
        """Wish video"""
        try:
            _video = self.get_video_from_request(self, request, *args, **kwargs)
            _valid_data = self.get_wish_fk(request.user, _video)
            serializer = self.get_serializer(data=_valid_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as error:
            # flatten error codes
            _error_codes = (
                error.get_codes() if isinstance(error.get_codes(), list) else list(*error.get_codes().values())
            )
            # error is from UniqueTogetherValidator
            if "unique" in _error_codes:
                raise WishAlreadyExistsException() from error
            # others
            raise error

    def destroy(self, request, *args, **kwargs):
        """Unwish video"""
        try:
            # validate user and video
            _video = self.get_video_from_request(self, request, *args, **kwargs)
            _valid_data = self.get_wish_fk(request.user, _video)
            # set user
            self.kwargs["user_id"] = request.user.id
            response = super().destroy(self, request, *args, **kwargs)  # type: Response
            return response
        except ResultNotFoundException as not_found:
            raise WishNotFoundException() from not_found
