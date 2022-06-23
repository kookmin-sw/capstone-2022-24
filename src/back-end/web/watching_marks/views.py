"""APIs of watching_marks application"""
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
from watching_marks.exceptions import (
    WatchingMarkAlreadyExistsException,
    WatchingMarkNotFoundException,
)
from watching_marks.schemas import WATCHINGMARK_LIST_EXAMPLES
from watching_marks.serializers import (
    WatchingMarkListSerializer,
    WatchingMarkSerializer,
)


# pylint: disable=R0901
@extend_schema(
    tags=["Priority-3", "User"],
    examples=WATCHINGMARK_LIST_EXAMPLES,
)
class WatchingMarkListView(ListAPIView):
    """watching mark apis of user's video history"""

    queryset = User.objects.prefetch_related("watchingmark_set", "watchingmark_set__user" "watchingmark_set__video")
    serializer_class = WatchingMarkListSerializer
    pagination_class = VideoHistoryPagination

    def get_queryset(self):
        """get login user's watching mark objects"""
        try:
            # (required) query parameters: videoLimit & videoOffset (used in pagination)
            if VideoHistoryPagination.limit_query_param not in self.request.query_params:
                raise InvalidPaginationParameterException()
            if VideoHistoryPagination.offset_query_param not in self.request.query_params:
                raise InvalidPaginationParameterException()
            # other query parameters are included
            if len(self.request.query_params) >= 3:
                raise InvalidPaginationParameterException()
            _queryset = self.request.user.watchingmark_set.order_by("-date_time")
            # user does not wathing mark any videos yet
            if not _queryset:
                raise WatchingMarkNotFoundException
            return _queryset
        except WatchingMarkNotFoundException as watching_mark_404:
            raise WatchingMarkNotFoundException from watching_mark_404

    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


@extend_schema_view(
    post=extend_schema(
        tags=["Priority-3", "User"],
        operation_id="관람표시 등록",
        description="Add watching mark list",
        request=None,
    ),
    delete=extend_schema(
        tags=["Priority-3", "User"], operation_id="관람 표시 취소", description="Delete from watching mark list"
    ),
)
class WatchingMarkCreateAndDestroyView(MultipleFieldLookupMixin, CreateAPIView, DestroyAPIView):
    """[POST & DELETE] /videos/{video_id}/watch-mark/"""

    queryset = Video.objects.prefetch_related("watchingmark_set", "watchingmark_set__user", "videototalcount")
    serializer_class = WatchingMarkSerializer
    permission_classes = (permissions.IsAuthenticated,)  # TODO
    lookup_fields = ("user_id", "video_id")

    def get_video_by_id(self, video_id):
        """Find video object among queryset by its id"""
        try:
            _queryset = self.queryset
            _video = _queryset.get(id=video_id)
            return _video
        except Video.objects.model.DoesNotExist as not_exist:
            raise VideoNotFoundException() from not_exist

    def get_queryset(self):
        """Get watching mark queryset belongs to video object"""
        _id = self.kwargs.get("video_id", None)
        _video = self.get_video_by_id(_id) if _id else None  # type: Video
        return _video.watchingmark_set

    def get_video_from_request(self, request, *args, **kwargs):
        """Validate user and video and return user, video dict"""
        try:
            _video_id = kwargs["video_id"]
            _video = self.get_video_by_id(_video_id)
        except KeyError as e:
            raise InvalidVideoIdException() from e
        return _video

    def get_watching_fk(self, user, video):
        """Get watching mark request detail with user, video ids"""
        return {"user": user.id, "video": video.id}

    def create(self, request, *args, **kwargs):
        """Watching Mark video"""
        try:
            _video = self.get_video_from_request(self, request, *args, **kwargs)
            _valid_data = self.get_watching_fk(request.user, _video)
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
                raise WatchingMarkAlreadyExistsException() from error
            # others
            raise error

    def destroy(self, request, *args, **kwargs):
        """Unwish video"""
        try:
            # validate user and video
            _video = self.get_video_from_request(self, request, *args, **kwargs)
            _valid_data = self.get_watching_fk(request.user, _video)
            # set user
            self.kwargs["user_id"] = request.user.id
            response = super().destroy(self, request, *args, **kwargs)  # type: Response
            return response
        except ResultNotFoundException as not_found:
            raise WatchingMarkNotFoundException() from not_found
