"""APIs of Video application : HomeView"""
# pylint: disable=R0914

from config.exceptions.input import BadFormatException
from config.exceptions.result import ResultNotFoundException
from django.db.models import Q
from drf_spectacular.utils import OpenApiParameter, OpenApiResponse, extend_schema
from rest_framework import permissions, status, viewsets
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
        OpenApiParameter(name="page", description="page number", type=int),
        OpenApiParameter(name="size", description="Number of videos to show on one page", type=int),
    ],
    responses={200: OpenApiResponse(description="검색 성공", response={"result"})},  # 어떻게 처리해야할지 잘 모르겠어서 임시처리
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

    def search(self, key):
        """Method : Process the Search fuction"""

        queryset = Video.objects.filter(Q(title__icontains=key))
        return queryset

    def list(self, request):
        """Method: Get Command to search, filter, sort"""

        """
        =======Searching=======
        Search : search by video title
        """

        search_target = self.request.query_params.get("search", default="")
        queryset = self.search(search_target)

        # Review
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

        queryset = Video.objects.filter(_filter)

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
            query = VideoProvider.objects.filter(Q(video=model)).values_list("provider__name")
            for video in query:
                provider_name = video[0]
                provider_list.append(provider_name)
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
