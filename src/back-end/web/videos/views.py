"""Video Api"""

import json
import os
import sys

import environ
import requests
from config.exceptions.input import BadFormatException
from config.exceptions.result import NoneResultException, NoneVideoException
from config.settings.base import ENV_DIR
from django.core.exceptions import FieldError
from django.core.paginator import Paginator
from django.db.models import Q
from drf_spectacular.utils import OpenApiParameter, OpenApiResponse, extend_schema
from providers.models import Provider
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from video_providers.models import VideoProvider
from videos.exceptions import WrongVideoIDException
from videos.models import Video


def setting_env():
    """Checking envrionment and Reading Env file"""

    if "prod" in sys.argv:
        environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.prod"))
        sys.argv.remove("prod")
    elif "dev" in sys.argv:
        environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.dev"))
        sys.argv.remove("dev")
    else:
        environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.local"))


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

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  # permission 처리

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
        try:
            queryset = Video.objects.filter(Q(title__icontains=key))
            return queryset
        except FieldError as e:
            raise BadFormatException() from e

    def filter_provider(self, key):
        """Method : Process the provider filter fuction"""
        subqueryset = VideoProvider.objects.filter(Q(provider=None))

        try:
            for item in key:
                provider_obj = Provider.objects.get(Q(name=item))
                subqueryset = subqueryset | provider_obj.videoprovider_set.all()
        except Provider.DoesNotExist as e:
            raise BadFormatException() from e

        video_list = Video.objects.filter(Q(id=None))
        for item in subqueryset.values("video"):
            video_list = video_list | Video.objects.filter(Q(id=item["video"]))

        return video_list

    def list(self, request):
        """Method: Get Command to search, filter, sort"""

        """
        =======Searching=======
        Search : search by video title

        """
        search_target = self.request.query_params.get("search", default="")
        queryset = self.search(search_target)

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

        try:
            if categories is not None:
                queryset = queryset.filter(Q(category=categories))
        except FieldError as e:
            raise BadFormatException() from e

        if providers is not None:
            providers = providers.split(",")
            query_provider = self.filter_provider(providers)
            queryset = queryset & query_provider

        """
        =======Sorting=======
        Sort : sort videos ramndomly
        """

        sort = self.request.query_params.get("sort", default="random")
        try:
            queryset = queryset.order_by(self.sort_dict[sort])
        except FieldError as e:
            raise BadFormatException() from e

        page = self.request.GET.get("page", default=1)
        size = self.request.GET.get("size", default=25)
        paginator = Paginator(queryset, size)
        page_obj = paginator.get_page(page)

        """=======Making Response======="""

        data_lists = []
        for model in page_obj.object_list:
            provider_list = []
            query = VideoProvider.objects.filter(Q(video=model))
            for video in query:
                provider_name = video.provider.get().name
                provider_list.append(provider_name)
            temp = {
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
            raise NoneResultException()

        context = {
            "results": data_lists,
            "page": {
                "current": int(page),
                "total_page": paginator.num_pages,
                "total_result": paginator.count,
            },
        }

        return Response(context, status=status.HTTP_200_OK)


@extend_schema(
    tags=["Priority-1", "Video"],
    operation_id="영화 상세 정보",
    responses={200: OpenApiResponse(description="상세 정보 출력 성공", response={"result"})},  # 임시처리
)
class DetailView(viewsets.ViewSet):
    """Class that displays a detail informations of Movie"""

    language = "ko"

    env = environ.Env(DEBUG=(bool, False))
    setting_env()
    api_key = env("MOVIE_API_KEY_V3")

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def movie_details(self, request, video_id):
        """Method : Get Command to give the Movie detail informations"""

        movie_id = video_id

        try:
            movie = Video.objects.get(Q(id=movie_id))
        except Video.DoesNotExist as e:
            raise NoneVideoException() from e

        if movie.category != "MV":
            raise WrongVideoIDException()

        """====Use Open API to Get detail info===="""

        key = movie.tmdb_id
        movie_url = f"https://api.themoviedb.org/3/movie/{key}?api_key={self.api_key}&language={self.language}"
        response = requests.get(movie_url)
        contents = response.text

        json_ob = json.loads(contents)
        overview = json_ob["overview"]

        movie_provider = VideoProvider.objects.filter(Q(video=movie))

        """======Making Response======"""

        provider_list = []

        for item in movie_provider:
            provider = {
                "name": item.provider.get().name,
                "logo_url": item.provider.get().logo_key,
                "link": item.link,
            }
            provider_list.append(provider)

        context = {
            "video_id": movie.id,
            "poster_url": movie.poster_key,
            "title": movie.title,
            "title_english": movie.title_english,
            "overview": overview,
            "providers": provider_list,
        }

        return Response(context, status=status.HTTP_200_OK)
