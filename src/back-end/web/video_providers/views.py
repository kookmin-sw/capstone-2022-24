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
from video_providers.serializers import VideoProviderSerializer


@extend_schema(
    tags=["Priority-1", "Video"],
    operation_id="홈화면 작품 목록",
    parameters=[
        OpenApiParameter(name="search", description="condtion of searching video title", type=str),
        OpenApiParameter(
            name="providers",
            description="condtion of filtering video providers : WC, AP, WV, NF, DP, multiple filtering = Use ','",
            type=str,
        ),
        OpenApiParameter(
            name="category",
            description="condtion of filtering video category : MV, TV, multiple filtering = Use ','",
            type=str,
        ),
        OpenApiParameter(
            name="genres",
            description=(
                "condtion of filtering video category : SF ,액션, 로맨스, 드라마, 판타지,스릴러,코미디,모험,미스터리,애니메이션,음악,가족,"
                "전쟁,공포,범죄,역사,다큐멘터리,TV 영화, multiple filtering = Use ','"
            ),
            type=str,
        ),
        OpenApiParameter(name="releaseDateMin", description="condtion of filtering video release date min", type=int),
        OpenApiParameter(name="releaseDateMax", description="condtion of filtering video release date max", type=int),
        OpenApiParameter(
            name="productionCountry", description="condtion of filtering video production country : KR, OTHER", type=str
        ),
        OpenApiParameter(name="sort", description="video sort condition : random, new, release", type=str),
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

    def day_30(self, request):
        """Method that displays a list of videos on the discontinue screen"""
        object = VideoProvider.objects.filter(
            Q(deadline__lte=self.DAY30_DEADLINE) & Q(deadline__gte=self.DAY15_DEADLINE)
        )
        serializer = VideoProviderSerializer(object, many=True)

        return Response(serializer.data)

    def day_15(self, request):
        """Method that displays a list of videos on the discontinue screen"""
        object = VideoProvider.objects.filter(
            Q(deadline__lte=self.DAY15_DEADLINE) & Q(deadline__gte=self.DAY7_DEADLINE)
        )
        serializer = VideoProviderSerializer(object, many=True)

        return Response(serializer.data)

    def day_7(self, request):
        """Method that displays a list of videos on the discontinue screen"""
        object = VideoProvider.objects.filter(Q(deadline__lte=self.DAY7_DEADLINE))
        serializer = VideoProviderSerializer(object, many=True)

        return Response(serializer.data)
