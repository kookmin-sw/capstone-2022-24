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

    def tv_details(self, request, video_id, season_id):
        """Method : Get Command to give the Tv Seasons detail informations"""

        tv_id = video_id

        try:
            TV = Video.objects.get(Q(id=tv_id))
        except Video.DoesNotExist as e:
            raise NoneVideoException() from e

        if TV.category != "MV":
            raise WrongVideoIDException()

        """====Use Open API to Get detail info===="""

        key = TV.tmdb_id
        movie_url = f"https://api.themoviedb.org/3/tv/{key}?api_key={self.api_key}&language={self.language}"
        response = requests.get(movie_url)
        contents = response.text

        json_ob = json.loads(contents)
        overview = json_ob["overview"]

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
            "overview": overview,
            "providers": provider_list,
        }

        return Response(context, status=status.HTTP_200_OK)
