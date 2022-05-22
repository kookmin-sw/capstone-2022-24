"""APIs of video providers application"""

from django.db.models import Q
from django.utils import timezone
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from rest_framework import permissions, serializers, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from video_providers.models import VideoProvider
from video_providers.schema import SCHEMA_VALUE


class DiscontinuityListPagination(LimitOffsetPagination):
    """Custom Pagenation Class to provide Video Home View List"""

    default_limit = 36


class DiscontinuityClass(viewsets.ViewSet):
    """Class that displays a list of videos on the discontinue screen"""

    permission_classes = (permissions.AllowAny,)
    DAY30_DEADLINE = timezone.now() + timezone.timedelta(30)
    DAY15_DEADLINE = timezone.now() + timezone.timedelta(15)
    DAY7_DEADLINE = timezone.now() + timezone.timedelta(7)

    def get_discontinue_videos_response(self, _filter, request):
        """Method that Make a Response list of videos on the discontinue screen"""
        video_object = (
            VideoProvider.objects.filter(_filter)
            .values("video__id", "video__title", "video__poster_key", "video__category")
            .distinct()
        )
        provider_object = (
            VideoProvider.objects.filter(_filter).values("video__id", "provider__name", "provider__logo_key").distinct()
        )

        paginator = DiscontinuityListPagination()
        page_obj = paginator.paginate_queryset(video_object, request)

        data_list = []
        for video in page_obj:
            provider_list = []
            for provider in provider_object:
                if video["video__id"] == provider["video__id"]:
                    provider_data = {
                        "name": provider["provider__name"],
                        "logo_key": provider["provider__logo_key"],
                    }
                    provider_list.append(provider_data)
            temp = {
                "id": video["video__id"],
                "title": video["video__title"],
                "category": video["video__category"],
                "poster_key": video["video__poster_key"],
                "providers": provider_list,
            }
            data_list.append(temp)

        context = {
            "results": data_list,
            "page": {
                "limit": paginator.limit,
                "offset": paginator.offset,
                "total_count": paginator.count,
            },
        }
        return context

    @extend_schema(
        tags=["Priority-2", "Video"],
        operation_id="30일이내 내려가는 작품 목록",
        parameters=[
            OpenApiParameter(name="limit", description="number of Videos to display", type=int),
            OpenApiParameter(name="offset", description="number of Videos list Start point", type=int),
        ],
        responses={
            200: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="videoListSerializer",
                    fields={"result": serializers.CharField()},
                ),
                description="작품 목록 제공 성공",
                examples=[OpenApiExample(response_only=True, name="Success Example", value=SCHEMA_VALUE)],
            )
        },
    )
    def get_discontinue_videos_after_30_days(self, request):
        """Method that displays a list of videos on the discontinue screen"""
        _filter = Q(deadline__lte=self.DAY30_DEADLINE) & Q(deadline__gt=self.DAY15_DEADLINE)
        context = self.get_discontinue_videos_response(_filter, request)
        return Response(context, status=status.HTTP_200_OK)

    @extend_schema(
        tags=["Priority-2", "Video"],
        operation_id="15일이내 내려가는 작품 목록",
        parameters=[
            OpenApiParameter(name="limit", description="number of Videos to display", type=int),
            OpenApiParameter(name="offset", description="number of Videos list Start point", type=int),
        ],
        responses={
            200: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="videoListSerializer",
                    fields={"result": serializers.CharField()},
                ),
                description="작품 목록 제공 성공",
                examples=[OpenApiExample(response_only=True, name="Success Example", value=SCHEMA_VALUE)],
            )
        },
    )
    def get_discontinue_videos_after_15_days(self, request):
        """Method that displays a list of videos on the discontinue screen"""
        _filter = Q(deadline__lte=self.DAY15_DEADLINE) & Q(deadline__gt=self.DAY7_DEADLINE)
        context = self.get_discontinue_videos_response(_filter, request)
        return Response(context, status=status.HTTP_200_OK)

    @extend_schema(
        tags=["Priority-2", "Video"],
        operation_id="7일이내 내려가는 작품 목록",
        parameters=[
            OpenApiParameter(name="limit", description="number of Videos to display", type=int),
            OpenApiParameter(name="offset", description="number of Videos list Start point", type=int),
        ],
        responses={
            200: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="videoListSerializer",
                    fields={"result": serializers.CharField()},
                ),
                description="작품 목록 제공 성공",
                examples=[OpenApiExample(response_only=True, name="Success Example", value=SCHEMA_VALUE)],
            )
        },
    )
    def get_discontinue_videos_after_7_days(self, request):
        """Method that displays a list of videos on the discontinue screen"""
        _filter = Q(deadline__lte=self.DAY7_DEADLINE)
        context = self.get_discontinue_videos_response(_filter, request)
        return Response(context, status=status.HTTP_200_OK)
