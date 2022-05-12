"""APIs of Video application : DetailView"""
# pylint: disable=R0914

import json

import requests
from config.exceptions.result import NoneVideoException
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from video_providers.models import VideoProvider
from videos.exceptions import WrongVideoIDException
from videos.models import Video


@extend_schema(
    tags=["Priority-1", "Video"],
    operation_id="TV 시즌1 기준으로 리다이렉트 조회",
    responses={302: OpenApiResponse(description="리다이렉트 성공", response={"result"})},  # 임시처리
)
def tv_season_redirect_view(request, video_id):
    """Method: redirect to TV details page"""

    return HttpResponseRedirect(reverse("tv_details", kwargs={"video_id": video_id, "season_num": 1}))


@extend_schema(
    tags=["Priority-1", "Video"],
    operation_id="TV 시즌 상세 정보",
    responses={200: OpenApiResponse(description="상세 정보 출력 성공", response={"result"})},  # 임시처리
)
class DetailView(viewsets.ViewSet):
    """Class that displays a detail informations of Movie"""

    language = "ko"

    api_key = settings.API_KEY_V3

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
            print(item.provider__provider)
            print(item.provider.values_list())
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

    def get_season_list(self, json_season):
        """Method: Get the Tv season lists"""

        season_list = []
        for item in json_season:
            season = {
                "number": item["season_number"],
                "name": item["name"],
            }
            season_list.append(season)

        return season_list

    def get_request_to_json(self, url):
        """Method: get json response to get video info"""
        response = requests.get(url)
        contents = response.text
        json_ob = json.loads(contents)

        return json_ob

    def tv_details(self, request, video_id, season_num):
        """Method : Get Command to give the Tv Seasons detail informations"""

        tv_id = video_id
        season_number = season_num

        try:
            TV = Video.objects.get(Q(id=tv_id))
        except Video.DoesNotExist as e:
            raise NoneVideoException() from e

        if TV.category != "TV":
            raise WrongVideoIDException()

        """====Use Open API to Get detail info===="""

        key = TV.tmdb_id
        tv_url = f"https://api.themoviedb.org/3/tv/{key}?api_key={self.api_key}&language={self.language}"
        tv_json_ob = self.get_request_to_json(tv_url)

        season_list = self.get_season_list(tv_json_ob["seasons"])  # 시즌 넘버, 시즌 네임 달려있어야함.

        tv_season_url = (
            f"https://api.themoviedb.org/3/tv/{key}/season/{season_number}"
            f"?api_key={self.api_key}&language={self.language}"
        )
        season_json_ob = self.get_request_to_json(tv_season_url)

        if "success" in season_json_ob:
            raise NoneVideoException()

        TV_provider = VideoProvider.objects.filter(Q(video=TV))

        """======Making Response======"""

        provider_list = []

        for item in TV_provider:
            provider = {
                "name": item.provider.get().name,
                "logo_url": item.provider.get().logo_key,
                "link": item.link,
            }
            provider_list.append(provider)

        context = {
            "video_id": TV.id,
            "poster_url": TV.poster_key,
            "title": TV.title,
            "title_english": TV.title_english,
            "overview": season_json_ob["overview"],
            "providers": provider_list,
            "total_seasons": tv_json_ob["number_of_seasons"],
            "total_episodes": tv_json_ob["number_of_episodes"],
            "seasons": season_list,
        }

        return Response(context, status=status.HTTP_200_OK)
