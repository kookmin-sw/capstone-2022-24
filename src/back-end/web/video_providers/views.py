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
from video_providers.serializers import DiscontinuityVideoSerializer


class DiscontinuityListPagination(LimitOffsetPagination):
    """Custom Pagenation Class to provide Video Home View List"""

    default_limit = 36


@extend_schema(
    tags=["Priority-2", "Video"],
    operation_id="내려가는 작품 목록",
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
            description="검색 성공",
            examples=[
                OpenApiExample(
                    response_only=True,
                    name="Success Example",
                    value={
                        "results": [
                            {
                                "videoId": 8,
                                "title": "인 비트윈",
                                "titleEnglish": "The In Between",
                                "posterKey": "https://image.tmdb.org/t/p/original/qcOFxYpBvU8LwaMyKdjCoP7y7we.jpg",
                                "filmRating": None,
                                "releaseDate": 2022,
                                "category": "MV",
                                "providers": ["NF"],
                            },
                            {
                                "videoId": 9,
                                "title": "수퍼 소닉",
                                "titleEnglish": "Sonic the Hedgehog",
                                "posterKey": "https://image.tmdb.org/t/p/original/pMXOlasWr1IzHGH8HWw1ZTXs6rQ.jpg",
                                "filmRating": None,
                                "releaseDate": 2020,
                                "category": "MV",
                                "providers": ["WC", "NF", "WC"],
                            },
                            {
                                "videoId": 10,
                                "title": "벤전스",
                                "titleEnglish": "Fistful of Vengeance",
                                "posterKey": "https://image.tmdb.org/t/p/original/3cccEF9QZgV9bLWyupJO41HSrOV.jpg",
                                "filmRating": None,
                                "releaseDate": 2022,
                                "category": "MV",
                                "providers": ["NF"],
                            },
                        ],
                        "page": {
                            "limit": 3,
                            "offset": 10,
                            "total_count": 176,
                        },
                    },
                )
            ],
        )
    },
)
class DiscontinuityClass(viewsets.ViewSet):
    """Class that displays a list of videos on the discontinue screen"""

    permission_classes = (permissions.AllowAny,)
    DAY30_DEADLINE = timezone.now() + timezone.timedelta(30)
    DAY15_DEADLINE = timezone.now() + timezone.timedelta(15)
    DAY7_DEADLINE = timezone.now() + timezone.timedelta(7)
    pagination_class = DiscontinuityListPagination

    def day_30(self, request):
        """Method that displays a list of videos on the discontinue screen"""
        _object = VideoProvider.objects.filter(
            Q(deadline__lte=self.DAY30_DEADLINE) & Q(deadline__gte=self.DAY15_DEADLINE)
        )
        serializer = DiscontinuityVideoSerializer(_object, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def day_15(self, request):
        """Method that displays a list of videos on the discontinue screen"""
        _object = VideoProvider.objects.filter(
            Q(deadline__lte=self.DAY15_DEADLINE) & Q(deadline__gte=self.DAY7_DEADLINE)
        )
        serializer = DiscontinuityVideoSerializer(_object, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def day_7(self, request):
        """Method that displays a list of videos on the discontinue screen"""
        _object = VideoProvider.objects.filter(Q(deadline__lte=self.DAY7_DEADLINE))
        serializer = DiscontinuityVideoSerializer(_object, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
