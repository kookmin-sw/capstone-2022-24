"""APIs of Video application : DetailView"""
# pylint: disable=R0914
import gettext
import json

import pycountry
import requests
from config.exceptions.result import VideoNotFoundException
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from drf_spectacular.utils import OpenApiResponse, extend_schema, inline_serializer
from rest_framework import permissions, serializers, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from tv_details.models import TvSeasonDetail
from video_providers.models import VideoProvider
from videos.exceptions import WrongVideoIDException
from videos.models import Genre, ProductionCountry, Video
from videos.schemas import DETAIL_MOVIE_VIEW_EXAMPLE, DETAIL_TV_VIEW_EXAMPLE
from watching_marks.models import WatchingMark
from wishes.models import Wish


@extend_schema(
    tags=["Priority-1", "Video"],
    operation_id="TV 시즌1 기준으로 리다이렉트 조회",
    responses={301: OpenApiResponse(description="첫번째 시즌으로 리다이렉트 조회")},
)
@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def tv_season_redirect_view(request, video_id):
    """Method: redirect to TV details page"""

    return HttpResponseRedirect(reverse("tv_details", kwargs={"video_id": video_id, "season_num": 1}))


class DetailView(viewsets.ViewSet):
    """Class that displays a detail informations of Movie, TV"""

    language = "ko"

    api_key = settings.API_KEY_V3

    permission_classes = (permissions.AllowAny,)

    category_title_naming = {"TV": "name", "MV": "title"}

    def get_season_list(self, series):
        """Method: Get the TV season data to lists"""

        season_list = []
        seasons = series.tvseason_set.all()
        for item in seasons:
            season_object = {"name": item.name, "number": item.number}
            season_list.append(season_object)

        return season_list

    def get_similar_list(self, similar_json, category_type):
        """Method: Get the similar video lists"""

        similar_list = []
        naming = self.category_title_naming[category_type]
        count = 0
        while len(similar_list) < 6 or similar_json["total_results"] == count:
            poster_path = similar_json["results"][count]["poster_path"]
            if poster_path:
                similar_video = {
                    "poster_url": f"https://image.tmdb.org/t/p/w500{poster_path}",
                    "title": similar_json["results"][count][naming],
                }
                similar_list.append(similar_video)
            count += 1

        return similar_list

    def get_request_to_json(self, url):
        """Method: get json response to get video info"""
        response = requests.get(url)
        contents = response.text
        json_ob = json.loads(contents)

        return json_ob

    def get_video_info(self, video_id):
        """Method: get to video info in DB"""
        video_provider = (
            VideoProvider.objects.filter(Q(video=video_id))
            .values_list(
                "link",
                "provider__name",
                "provider__logo_key",
            )
            .distinct()
        )

        video_genre = Genre.objects.filter(Q(video=video_id)).values_list("name")
        video_production_country = ProductionCountry.objects.filter(Q(video=video_id)).values_list("name")

        video_info = {
            "video_provider": video_provider,
            "video_genre": video_genre,
            "video_production_country": video_production_country,
        }

        return video_info

    def make_video_response(self, video_info_list):
        """Method : Make video info list to video info response"""
        provider_list = []

        for item in video_info_list["video_provider"]:
            provider = {
                "name": item[1],
                "logo_url": item[2],
                "link": item[0],
            }
            provider_list.append(provider)

        genre_list = []
        for item in video_info_list["video_genre"]:
            genre_list.append(item[0])

        production_country_list = []
        get = gettext.translation("iso3166", pycountry.LOCALES_DIR, languages=["ko"])
        get.install()
        for item in video_info_list["video_production_country"]:
            country_name = get.gettext(pycountry.countries.get(alpha_2=item[0]).name)
            production_country_list.append(country_name)

        return {
            "provider_list": provider_list,
            "genre_list": genre_list,
            "production_country_list": production_country_list,
        }

    def video_personal_count(self, request_user, video_id, context):
        """Method : Check whether the User Personal info : Wished, Watched"""

        try:
            Wish.objects.get(Q(video=video_id) & Q(user=request_user))
            wished = True
        except Wish.DoesNotExist:
            wished = False

        try:
            WatchingMark.objects.get(Q(video=video_id) & Q(user=request_user))
            watched = True
        except WatchingMark.DoesNotExist:
            watched = False

        context["personal"] = {"wished": wished, "watched": watched}

        return context

    @extend_schema(
        tags=["Priority-1", "Video"],
        operation_id="TV 시즌 상세 정보",
        request=None,
        responses={
            200: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="tvSeason1Serializer",
                    fields={"result": serializers.CharField()},
                ),
                description="Success Example",
                examples=DETAIL_TV_VIEW_EXAMPLE,
            ),
            400: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="tvSeason2Serializer",
                    fields={"detail": serializers.CharField()},
                ),
                description="작품 종류와 다른 작품 ID 입력",
            ),
            404: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="tvSeason3Serializer",
                    fields={"detail": serializers.CharField()},
                ),
                description="없는 작품 ID 입력",
            ),
        },
    )
    def tv_details(self, request, video_id, season_num):
        """Method : Get Command to give the Tv Seasons detail informations"""

        tv_id = video_id
        season_number = season_num

        try:
            tv = Video.objects.prefetch_related(
                "tvseriesdetail",
                "videototalcount",
                "tvseriesdetail__tvseasondetail_set",
                "tvseriesdetail__tvseason_set",
            ).get(Q(id=tv_id))
        except Video.DoesNotExist as e:
            raise VideoNotFoundException() from e

        if tv.category != "TV":
            raise WrongVideoIDException()

        key = tv.tmdb_id
        try:
            season_data = tv.tvseriesdetail.tvseasondetail_set.get(Q(number=season_number))
        except TvSeasonDetail.DoesNotExist as e:
            raise VideoNotFoundException() from e

        season_list = self.get_season_list(tv.tvseriesdetail)
        tv_info_list = self.get_video_info(tv_id)

        """====Use Open API to Get similar list===="""

        tv_similar_url = (
            f"https://api.themoviedb.org/3/tv/{key}/similar?api_key={self.api_key}&language={self.language}"
        )
        tv_similar_json_ob = self.get_request_to_json(tv_similar_url)
        similar_list = self.get_similar_list(tv_similar_json_ob, tv.category)

        """======Making Response======"""
        tv_info_response = self.make_video_response(tv_info_list)

        context = {
            "video_id": tv.id,
            "poster_url": tv.poster_key,
            "title": tv.title,
            "title_english": tv.title_english,
            "release_year": str(tv.release_date.year),
            "release_date": tv.release_date.strftime("%m-%d"),
            "film_rating": tv.film_rating,
            "overview": season_data.overview,
            "providers": tv_info_response["provider_list"],
            "genres": tv_info_response["genre_list"],
            "production_countries": tv_info_response["production_country_list"],
            "total_seasons": tv.tvseriesdetail.number_of_seasons,
            "total_episodes": tv.tvseriesdetail.number_of_episodes,
            "trailer_url": season_data.trailer_key,
            "seasons": season_list,
            "public": {
                "wish_count": tv.videototalcount.wish_count,
                "watch_count": tv.videototalcount.watch_count,
            },
            "personal": {"wished": None, "watched": None},
            "similars": similar_list,
        }

        if request.user.is_authenticated:
            context = self.video_personal_count(request.user, tv.id, context)

        return Response(context, status=status.HTTP_200_OK)

    @extend_schema(
        tags=["Priority-1", "Video"],
        operation_id="영화 상세 정보",
        responses={
            200: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="movie1Serializer",
                    fields={"result": serializers.CharField()},
                ),
                description="상세 정보 출력 성공",
                examples=DETAIL_MOVIE_VIEW_EXAMPLE,
            ),
            400: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="movie2Serializer",
                    fields={"detail": serializers.CharField()},
                ),
                description="작품 종류와 다른 작품 ID 입력",
            ),
            404: OpenApiResponse(
                response=inline_serializer(
                    # meaningless serializer. Just Use to make the example visible
                    name="movie3Serializer",
                    fields={"detail": serializers.CharField()},
                ),
                description="없는 작품 ID 입력",
            ),
        },
    )
    def movie_details(self, request, video_id):
        """Method : Get Command to give the Movie detail informations"""

        movie_id = video_id

        try:
            movie = Video.objects.prefetch_related("moviedetail", "videototalcount").get(Q(id=movie_id))
        except Video.DoesNotExist as e:
            raise VideoNotFoundException() from e

        if movie.category != "MV":
            raise WrongVideoIDException()

        key = movie.tmdb_id
        movie_info_list = self.get_video_info(movie_id)

        """====Use Open API to Get similar list===="""

        movie_similar_url = (
            f"https://api.themoviedb.org/3/movie/{key}/similar?api_key={self.api_key}&language={self.language}"
        )
        movie_similar_json_ob = self.get_request_to_json(movie_similar_url)

        similar_list = self.get_similar_list(movie_similar_json_ob, movie.category)

        """======Making Response======"""

        movie_info_response = self.make_video_response(movie_info_list)

        context = {
            "video_id": movie.id,
            "poster_url": movie.poster_key,
            "title": movie.title,
            "release_year": str(movie.release_date.year),
            "release_date": movie.release_date.strftime("%m-%d"),
            "title_english": movie.title_english,
            "overview": movie.moviedetail.overview,
            "providers": movie_info_response["provider_list"],
            "genres": movie_info_response["genre_list"],
            "production_countries": movie_info_response["production_country_list"],
            "trailer_url": movie.moviedetail.trailer_key,
            "public": {
                "wish_count": movie.videototalcount.wish_count,
                "watch_count": movie.videototalcount.watch_count,
            },
            "personal": {"wished": None, "watched": None},
            "similars": similar_list,
        }

        if request.user.is_authenticated:
            context = self.video_personal_count(request.user, movie.id, context)

        return Response(context, status=status.HTTP_200_OK)
