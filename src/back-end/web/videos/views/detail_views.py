"""APIs of Video application : DetailView"""
# pylint: disable=R0914

import json

import requests
from config.exceptions.result import VideoNotFoundException
from django.conf import settings
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from rest_framework import permissions, serializers, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from video_providers.models import VideoProvider
from videos.exceptions import WrongVideoIDException
from videos.models import Video


@extend_schema(
    tags=["Priority-1", "Video"],
    operation_id="TV 시즌1 기준으로 리다이렉트 조회",
    responses={301: OpenApiResponse(description="첫번째 시즌으로 리다이렉트 조회")},
)
@api_view(["GET"])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def tv_season_redirect_view(request, video_id):
    """Method: redirect to TV details page"""

    return HttpResponseRedirect(reverse("tv_details", kwargs={"video_id": video_id, "season_num": 1}))


class DetailView(viewsets.ViewSet):
    """Class that displays a detail informations of Movie"""

    language = "ko"

    api_key = settings.API_KEY_V3

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
                examples=[
                    OpenApiExample(
                        response_only=True,
                        name="Success Example",
                        value={
                            "videoId": 99,
                            "posterUrl": "https://image.tmdb.org/t/p/original/4EYPN5mVIhKLfxGruy7Dy41dTVn.jpg",
                            "title": "루시퍼",
                            "titleEnglish": "Lucifer",
                            "overview": "지옥에서 도망 나온 어머니의 방문에도, 악마답지 않은 자유분방함을 유지할 수 있을까?",
                            "providers": [
                                {
                                    "name": "NF",
                                    "logoUrl": "https://image.tmdb.org/t/p/original/9A1JSVmSxsyaBK4SUFsYVqbAYfW.jpg",
                                    "link": "https://www.netflix.com/kr/",
                                }
                            ],
                            "totalSeasons": 6,
                            "totalEpisodes": 93,
                            "seasons": [
                                {"number": 0, "name": "스페셜"},
                                {"number": 1, "name": "시즌 1"},
                                {"number": 2, "name": "시즌 2"},
                                {"number": 3, "name": "시즌 3"},
                                {"number": 4, "name": "시즌 4"},
                                {"number": 5, "name": "시즌 5"},
                                {"number": 6, "name": "시즌 6"},
                            ],
                        },
                    )
                ],
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
    def tv_details(self, request, video_id, season_num):
        """Method : Get Command to give the Tv Seasons detail informations"""

        tv_id = video_id
        season_number = season_num

        try:
            tv = Video.objects.get(Q(id=tv_id))
        except Video.DoesNotExist as e:
            raise VideoNotFoundException() from e

        if tv.category != "TV":
            raise WrongVideoIDException()

        """====Use Open API to Get detail info===="""

        key = tv.tmdb_id
        tv_url = f"https://api.themoviedb.org/3/tv/{key}?api_key={self.api_key}&language={self.language}"
        tv_json_ob = self.get_request_to_json(tv_url)

        season_list = self.get_season_list(tv_json_ob["seasons"])

        tv_season_url = (
            f"https://api.themoviedb.org/3/tv/{key}/season/{season_number}"
            f"?api_key={self.api_key}&language={self.language}"
        )
        season_json_ob = self.get_request_to_json(tv_season_url)

        if "success" in season_json_ob:
            raise VideoNotFoundException()

        tv_provider = VideoProvider.objects.filter(Q(video=tv)).values_list(
            "link", "provider__name", "provider__logo_key"
        )

        """======Making Response======"""

        provider_list = []

        for item in tv_provider:
            provider = {
                "name": item[1],
                "logo_url": item[2],
                "link": item[0],
            }
            provider_list.append(provider)

        context = {
            "video_id": tv.id,
            "poster_url": tv.poster_key,
            "title": tv.title,
            "title_english": tv.title_english,
            "release_date": tv.release_date,
            "overview": season_json_ob["overview"],
            "providers": provider_list,
            "total_seasons": tv_json_ob["number_of_seasons"],
            "total_episodes": tv_json_ob["number_of_episodes"],
            "seasons": season_list,
        }

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
                examples=[
                    OpenApiExample(
                        response_only=True,
                        name="Success Example",
                        value={
                            "videoId": 3,
                            "posterUrl": "https://image.tmdb.org/t/p/original/1Lh9LER4xRQ3INFFi2dfS2hpRwv.jpg",
                            "title": "베놈 2: 렛 데어 비 카니지",
                            "titleEnglish": "Venom: Let There Be Carnage",
                            "overview": (
                                "‘베놈'과 완벽한 파트너가 된 ‘에디 브록' 앞에 ‘클리터스 캐서디'가 ‘카니지'로 등장, "
                                "앞으로 닥칠 대혼돈의 세상을 예고한다. 대혼돈의 시대가 시작되고, 악을 악으로 처단할 것인가?"
                            ),
                            "providers": [
                                {
                                    "name": "NF",
                                    "logoUrl": "https://image.tmdb.org/t/p/original/9A1JSVmSxsyaBK4SUFsYVqbAYfW.jpg",
                                    "link": "https://www.netflix.com/kr/",
                                },
                                {
                                    "name": "WC",
                                    "logoUrl": "https://image.tmdb.org/t/p/original/cNi4Nv5EPsnvf5WmgwhfWDsdMUd.jpg",
                                    "link": "https://www.wavve.com/",
                                },
                            ],
                        },
                    )
                ],
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
            movie = Video.objects.get(Q(id=movie_id))
        except Video.DoesNotExist as e:
            raise VideoNotFoundException() from e

        if movie.category != "MV":
            raise WrongVideoIDException()

        """====Use Open API to Get detail info===="""

        key = movie.tmdb_id
        movie_url = f"https://api.themoviedb.org/3/movie/{key}?api_key={self.api_key}&language={self.language}"
        json_ob = self.get_request_to_json(movie_url)
        overview = json_ob["overview"]

        movie_provider = VideoProvider.objects.filter(Q(video=movie)).values_list(
            "link", "provider__name", "provider__logo_key"
        )

        """======Making Response======"""

        provider_list = []

        for item in movie_provider:
            provider = {
                "name": item[1],
                "logo_url": item[2],
                "link": item[0],
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
