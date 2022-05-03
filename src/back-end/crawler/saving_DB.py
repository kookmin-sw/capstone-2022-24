"""Save the data in the actual DB"""

import json
import os
import sys

from arrange_data import (
    arrange_movie_data,
    arrange_movie_detail,
    arrange_movie_provider,
    arrange_tv_data,
    arrange_tv_detail,
    arrange_tv_provider,
)

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.config.settings")
import django

django.setup()

from djongo.models import Q

# 여기가 models.py에서 설계한 모델을 가져오는 코드입니다
from web.providers.models import Provider
from web.video_providers.models import VideoProvider
from web.videos.models import Genre, ProductionCountry, Video, VideoDetail


def saving_video_data(video_data):
    """Method: Save the data in Video model"""
    for item in video_data:
        Video(
            tmdb_id=item["tmdb_id"],
            title=item["title"],
            release_date=item["release_date"],
            film_rating=item["film_rating"],
            category=item["category"],
            poster_key=item["poster_url"],
            title_english=item["title_english"],
        ).save()


def saving_detail_data(video_detail_data):
    """Method: Save the data in VideoDetail model"""
    for item in video_detail_data:
        video_id = Video.object.get(Q(category=item["category"]) & Q(tmdb_id=item["tmbd_id"]))
        VideoDetail(video=video_id, runtime=item["runtime"]).save()


def saving_genre_data(video_genre_data):
    """Method: Save the data in Genre model"""

    for item in video_genre_data:
        video_id = Video.object.get(Q(category=item["category"]) & Q(tmdb_id=item["tmbd_id"]))
        genre_list = item["genres"]
        for gerne in genre_list:
            Genre(video=video_id, name=gerne).save()


def saving_production_country_data(video_production_country_data):
    """Method: Save the data in ProductionCountry model"""

    for item in video_production_country_data:
        video_id = Video.objects.get(Q(category=item["category"]) & Q(tmdb_id=item["tmbd_id"]))
        for country in item["production_countries"]:
            ProductionCountry(video=video_id, name=country).save()


def saving_provider_data(video_provider_data):
    """Method: Save the data in VideoProvider model"""

    for item in video_provider_data:
        video_id = Video.object.get(Q(category=item["category"]) & Q(tmdb_id=item["tmbd_id"]))
        provider_list = item["providers"]
        for obj in provider_list:
            provider_id = Provider.objects.get(Q(tmdb_id=obj["provider_id"]))
            VideoProvider(
                video=video_id,
                provider=provider_id,
                offer_type=obj["offer_type"],
                link=obj["link"],
                offer_date=obj["crawling_time"],
                deadline=obj[""],
            ).save()


if __name__ == "__main__":
    file_movie_path = "/Moviesample.json"

    with open(file_movie_path, "r", encoding="utf8") as file:
        contents = file.read()
        json_movie_dict = json.loads(contents)

    """movie data saving to video model"""
    movie_data = arrange_movie_data(json_movie_dict)
    movie_detail_data, movie_genre_data, movie_production_country_data = arrange_movie_detail(json_movie_dict)
    movie_provider_data = arrange_movie_provider(json_movie_dict)

    saving_video_data(movie_data)
    saving_detail_data(movie_detail_data)
    saving_genre_data(movie_genre_data)
    saving_production_country_data(movie_production_country_data)
    saving_provider_data(movie_provider_data)

    file_movie_path = "/tvsample.json"

    with open(file_movie_path, "r", encoding="utf8") as file:
        contents = file.read()
        json_tv_dict = json.loads(contents)

    """movie data saving to video model"""
    tv_data = arrange_tv_data(json_tv_dict)
    tv_detail_data, tv_genre_data, tv_production_country_data = arrange_tv_detail(json_tv_dict)
    tv_provider_data = arrange_tv_provider(json_tv_dict)

    saving_video_data(tv_data)
    saving_detail_data(tv_detail_data)
    saving_genre_data(tv_genre_data)
    saving_production_country_data(tv_production_country_data)
    saving_provider_data(tv_provider_data)
