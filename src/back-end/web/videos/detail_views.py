"""APIs of Video application : DetailView"""
# pylint: disable=R0914

import json
import os
import sys

import environ
import requests
from config.exceptions.result import NoneVideoException
from config.settings.base import ENV_DIR
from django.db.models import Q
from drf_spectacular.utils import OpenApiResponse, extend_schema
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
    operation_id="TV 시즌 상세 정보",
    responses={200: OpenApiResponse(description="상세 정보 출력 성공", response={"result"})},  # 임시처리
)
class DetailView(viewsets.ViewSet):
    """Class that displays a detail informations of Movie"""

    language = "ko"

    env = environ.Env(DEBUG=(bool, False))
    setting_env()
    api_key = env("MOVIE_API_KEY_V3")

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

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
