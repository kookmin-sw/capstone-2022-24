import os
from datetime import datetime

from crawler_base import check_vaild, none_providers_list, watch_providers

## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websaver.settings")
## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django

django.setup()

from web.providers.models import Provider
from web.video_providers.models import VideoProvider

# 여기가 models.py에서 설계한 모델을 가져오는 코드입니다
from web.videos.models import Video, VideoDetail


def arrange_movie_data(dicts):
    """method: 영화 기본정보 분류하는 file"""

    result = []

    for key, value in dicts.items():
        tmdb_id = key
        movie_data = value[1]

        try:
            date_time_str = movie_data["release_date"]
            date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d").date()
        except:
            date_time_obj = None

        poster_path = check_vaild(movie_data, "poster_path")

        if poster_path is not None:
            poster_url = f"https://image.tmdb.org/t/p/original{poster_path}"

        title_english = check_vaild(movie_data, "original_title")

        object_movie = {
            "tmdb_id": tmdb_id,
            "title": movie_data["title"],
            "release_date": date_time_obj,
            "film_rating": None,
            "category": "MV",
            "poster_url": poster_url,
            "title_english": title_english,
        }
        result.append(object_movie)

    return result


def arrange_movie_detail(dicts):
    """method: 영화 세부정보, 장르, 제작국가 분류하는 file"""

    detail_list = []
    genre_list = []
    production_country_list = []

    for key, value in dicts.items():
        tmdb_id = key
        movie_data = value[1]

        """디테일 정보 정리"""
        runtime = check_vaild(movie_data, "runtime")

        object_detail = {
            "tmdb_id": tmdb_id,
            "category": "MV",
            "runtime": runtime,
        }
        detail_list.append(object_detail)

        """장르 정보 정리"""
        genres = []
        genre_data = check_vaild(movie_data, "genres")
        for itme in genre_data:
            genres.append(itme["name"])

        object_genre = {
            "tmdb_id": tmdb_id,
            "category": "MV",
            "genres": genres,
        }
        genre_list.append(object_genre)

        """생산 국가 정리"""
        production_countries = []
        production_country_data = check_vaild(movie_data, "production_countries")

        for item in production_country_data:
            production_countries.append(item["iso_3166_1"])

        object_production_country = {
            "tmdb_id": tmdb_id,
            "category": "MV",
            "production_countries": production_countries,
        }
        production_country_list.append(object_production_country)

    return detail_list, genre_list, production_country_list


def arrange_movie_provider(dicts):
    """method: 영화 provider을 분류하는 file"""

    provider_list = []
    for key, value in dicts.items():
        tmdb_id = key
        movie_data = value[2]["providers"]

        offer_type_list = list(movie_data.keys())
        offer_type_list.remove("link")

        providers = []
        for item in offer_type_list:
            for iter in movie_data[item]:
                if str(iter["provider_id"]) in watch_providers:
                    provider = {
                        "offerType": item,
                        "providerid": iter["provider_id"],
                    }
                    providers.append(provider)

        object_providers = {
            "tmdb_id": tmdb_id,
            "category": "MV",
            "providers": providers,
        }
        provider_list.append(object_providers)

    return provider_list
