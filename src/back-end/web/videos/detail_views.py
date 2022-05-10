"""APIs of Video application : DetailView"""
# pylint: disable=R0914

import os
import sys

import environ
from config.settings.base import ENV_DIR
from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

# from videos.exceptions import WrongVideoIDException


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

        """======Making Response======"""
        context = {
            "video_id": video_id,
            "poster_url": 0,
            "title": 0,
            "title_english": 0,
            "overview": 0,
            "providers": 0,
        }

        return Response(context, status=status.HTTP_200_OK)
