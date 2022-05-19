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
from videos.exceptions import WrongVideoIDException
from videos.models import Video
from wishes.models import Wish


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

    def get_video_info(self, video_id):
        """Method: get to video info in DB"""
        video_provider = (
            Video.objects.filter(Q(id=video_id))
            .values_list(
                "videoprovider__link",
                "videoprovider__provider__name",
                "videoprovider__provider__logo_key",
            )
            .distinct()
        )

        video_genre = Video.objects.filter(Q(id=video_id)).values_list("genre__name")
        video_production_country = Video.objects.filter(Q(id=video_id)).values_list("productioncountry__name")

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
        for item in video_info_list["video_production_country"]:
            production_country_list.append(item[0])

        return {
            "provider_list": provider_list,
            "genre_list": genre_list,
            "production_country_list": production_country_list,
        }

    def video_personal_count(self, request_user, video_id, context):
        """user가 로그인 했을 경우 context에 추가 값을 입력해주는 메소드"""

        try:
            Wish.objects.get(Q(video=video_id) & Q(user=request_user))
            wished = True
        except Wish.DoesNotExist:
            wished = False

        context["personal"] = {"wished": wished}

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
                examples=[
                    OpenApiExample(
                        response_only=True,
                        name="Success Example",
                        value={
                            "videoId": 200,
                            "posterUrl": "https://image.tmdb.org/t/p/w500/ekp9PbSODHiTXXqnHJ4Sq6YHkhq.jpg",
                            "title": "블리치",
                            "titleEnglish": "Bleach",
                            "releaseDate": "2004-10-05",
                            "filmRating": None,
                            "overview": "",
                            "providers": [
                                {
                                    "name": "WV",
                                    "logoUrl": "https://image.tmdb.org/t/p/original/cNi4Nv5EPsnvf5WmgwhfWDsdMUd.jpg",
                                    "link": "https://www.wavve.com/",
                                }
                            ],
                            "genres": ["Action & Adventure", "애니메이션", "Sci-Fi & Fantasy"],
                            "productionCountries": ["JP"],
                            "totalSeasons": 1,
                            "totalEpisodes": 366,
                            "seasons": [{"number": 0, "name": "스페셜"}, {"number": 1, "name": "시즌 1"}],
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

        tv_info_list = self.get_video_info(tv_id)

        """======Making Response======"""

        tv_info_response = self.make_video_response(tv_info_list)

        context = {
            "video_id": tv.id,
            "poster_url": tv.poster_key,
            "title": tv.title,
            "title_english": tv.title_english,
            "release_date": tv.release_date,
            "film_rating": tv.film_rating,
            "overview": season_json_ob["overview"],
            "providers": tv_info_response["provider_list"],
            "genres": tv_info_response["genre_list"],
            "production_countries": tv_info_response["production_country_list"],
            "total_seasons": tv_json_ob["number_of_seasons"],
            "total_episodes": tv_json_ob["number_of_episodes"],
            "seasons": season_list,
            "public": {"wish_count": tv.videototalcount.wish_count},
        }

        context["personal"] = {"wished": None}

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
                examples=[
                    OpenApiExample(
                        response_only=True,
                        name="Success Example",
                        value={
                            "videoId": 8,
                            "posterUrl": "https://image.tmdb.org/t/p/w500/zDNAeWU0PxKolEX1D8Vn1qWhGjH.jpg",
                            "title": "인터스텔라",
                            "releaseDate": "2014-11-05",
                            "titleEnglish": "Interstellar",
                            "overview": (
                                "세계 각국의 정부와 경제가 완전히 붕괴된 미래가 다가온다. 지난 20세기에 범한 잘못이"
                                "전 세계적인 식량 부족을 불러왔고, NASA도 해체되었다. 나사 소속 우주비행사였던 쿠퍼는 지구에 몰아친 식량난으로 옥수수나 키우며 살고 있다."
                                "거센 황사가 몰아친 어느 날 알 수 없는 힘에 이끌려 딸과 함께 도착한 곳은 인류가 이주할 행성을 찾는 나사의 비밀본부."
                                "이 때 시공간에 불가사의한 틈이 열리고, 이 곳을 탐험해 인류를 구해야 하는 임무를 위해 쿠퍼는 만류하는 딸을 뒤로한 채 우주선에 탑승하는데..."
                            ),
                            "providers": [
                                {
                                    "name": "NF",
                                    "logoUrl": "https://image.tmdb.org/t/p/original/9A1JSVmSxsyaBK4SUFsYVqbAYfW.jpg",
                                    "link": "https://www.netflix.com/kr/",
                                },
                                {
                                    "name": "WV",
                                    "logoUrl": "https://image.tmdb.org/t/p/original/cNi4Nv5EPsnvf5WmgwhfWDsdMUd.jpg",
                                    "link": "https://www.wavve.com/",
                                },
                                {
                                    "name": "WC",
                                    "logoUrl": "https://image.tmdb.org/t/p/original/dgPueyEdOwpQ10fjuhL2WYFQwQs.jpg",
                                    "link": "https://watcha.com/",
                                },
                            ],
                            "genres": ["모험", "드라마", "SF"],
                            "productionCountries": ["GB", "US"],
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

        movie_info_list = self.get_video_info(movie_id)

        """======Making Response======"""

        movie_info_response = self.make_video_response(movie_info_list)

        context = {
            "video_id": movie.id,
            "poster_url": movie.poster_key,
            "title": movie.title,
            "release_date": movie.release_date,
            "title_english": movie.title_english,
            "overview": overview,
            "providers": movie_info_response["provider_list"],
            "genres": movie_info_response["genre_list"],
            "production_countries": movie_info_response["production_country_list"],
            "public": {"wish_count": movie.videototalcount.wish_count},
        }

        context["personal"] = {"wished": None}

        if request.user.is_authenticated:
            context = self.video_personal_count(request.user, movie.id, context)

        return Response(context, status=status.HTTP_200_OK)
