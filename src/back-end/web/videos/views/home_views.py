"""APIs of Video application : HomeView"""
# pylint: disable=R0914

from config.exceptions.input import BadFormatException
from config.exceptions.result import ResultNotFoundException
from django.db.models import Q
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
from videos.models import Video


class VideoListPagination(LimitOffsetPagination):
    """Custom Pagenation Class to provide Video Home View List"""

    default_limit = 24


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
        OpenApiParameter(name="category", description="condtion of filtering video category : MV, TV", type=str),
        OpenApiParameter(name="sort", description="video sort condition : Use only only random", type=str),
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
class HomeView(viewsets.ViewSet):
    """Class that displays a list of videos on the home screen"""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    sort_dict = {
        "random": "id",
        "new": "offer_date",
        "release": "release_date",
        "wish": "wishes_count",
        "star": "star_count",
        "rating": "rating",
    }

    def list(self, request):
        """Method: Get Command to search, filter, sort"""

        """
        =======Searching=======
        Search : search by video title
        """

        search_target = self.request.query_params.get("search", default="")

        _filter = Q(title__icontains=search_target)

        """
        =======filtering=======
        Filter : OR operation within the conditions, AND operation between conditions.
                filter video by providers, categories
        """

        providers = self.request.query_params.get("providers", None)
        categories = self.request.query_params.get("category", None)

        """
        #아직 구현예정이 없는 필터링 조건
        genres = self.request.query_params.get('genres', None)
        rating_min = self.request.query_params.get('ratingMin', None)
        rating_max = self.request.query_params.get('ratingMax', None)
        runtime_min = self.request.query_params.get('runtimeMin', None)
        runtime_max = self.request.query_params.get('runtimeMax', None)
        release_date_min = self.request.query_params.get('releaseDateMin', None)
        release_date_max = self.request.query_params.get('releaseDateMax', None)
        production_country= self.request.query_params.get('productionCountry', None)
        offer_type = self.request.query_params.get('offerTye', None)
        watched = self.request.query_params.get('watched', None)
        """

        if categories:
            _filter &= Q(category=categories)

        if providers:
            _p = providers.split(",")
            _filter &= Q(videoprovider__provider__name__in=_p)

        queryset = Video.objects.filter(_filter).distinct()

        """
        =======Sorting=======
        Sort : sort videos ramndomly
        """

        sort = self.request.query_params.get("sort", default="random")
        try:
            if sort:
                queryset = queryset.order_by(self.sort_dict[sort])
        except KeyError as e:
            raise BadFormatException() from e

        paginator = VideoListPagination()
        page_obj = paginator.paginate_queryset(queryset, request)

        """=======Making Response======="""

        data_lists = []
        for model in page_obj:
            provider_list = []
            query = VideoProvider.objects.filter(Q(video=model)).values_list("provider__name").distinct()
            for video in query:
                _p = video[0]
                provider_list.append(_p)
            temp = {
                "video_id": model.id,
                "title": model.title,
                "title_english": model.title_english,
                "poster_key": model.poster_key,
                "film_rating": model.film_rating,
                "release_date": model.release_date.year,
                "category": model.category,
                "providers": provider_list,
            }
            data_lists.append(temp)

        if len(data_lists) == 0:
            raise ResultNotFoundException()

        context = {
            "results": data_lists,
            "page": {
                "limit": paginator.limit,
                "offset": paginator.offset,
                "total_count": paginator.count,
            },
        }

        return Response(context, status=status.HTTP_200_OK)