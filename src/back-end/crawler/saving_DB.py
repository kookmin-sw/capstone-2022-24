"""Save the data in the actual DB"""

import json
import os
import sys

import environ

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from web.config.settings.base import ENV_DIR

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=os.path.join(ENV_DIR, ".env.local"))

DEBUG = True
import MySQLdb
from arrange_data import (
    arrange_movie_data,
    arrange_movie_detail,
    arrange_movie_provider,
    arrange_tv_data,
    arrange_tv_detail,
    arrange_tv_provider,
)

"""==========Model for Saving data==========="""


def saving_video_data(video_data):
    """Method: Save the data in Video model"""
    for item in video_data:
        sql = "INSERT INTO videos (tmdb_id, title, release_date, film_rating,category,poster_key,title_english) VALUES (%s, %s, %s,%s,%s,%s,%s)"
        values = (
            item["tmdb_id"],
            item["title"],
            item["release_date"],
            item["film_rating"],
            item["category"],
            item["poster_url"],
            item["title_english"],
        )
        cursor.execute(sql, values)
        conn.commit()


def saving_detail_data(video_detail_data):
    """Method: Save the data in VideoDetail model"""
    for item in video_detail_data:
        sql_id = "SELECT id FROM videos WHERE tmdb_id =%s AND category= %s"
        values_id = (item["tmdb_id"], item["category"])
        cursor.execute(sql_id, values_id)
        video_id = cursor.fetchall()[0][0]

        sql = "INSERT INTO video_details (video_id, runtime) VALUES (%s, %s)"
        values = (
            video_id,
            item["runtime"],
        )
        print(sql)
        print(values)
        cursor.execute(sql, values)
        conn.commit()


def saving_genre_data(video_genre_data):
    """Method: Save the data in Genre model"""
    for item in video_genre_data:
        sql_id = "SELECT id FROM videos WHERE tmdb_id =%s AND category= %s"
        values_id = (item["tmdb_id"], item["category"])
        cursor.execute(sql_id, values_id)
        video_id = cursor.fetchall()[0][0]

        genre_list = item["genres"]
        for gerne in genre_list:
            sql = "INSERT INTO genres (video_id, name) VALUES (%s, %s)"
            values = (video_id, gerne)
            cursor.execute(sql, values)
            conn.commit()


def saving_production_country_data(video_production_country_data):
    """Method: Save the data in ProductionCountry model"""
    for item in video_production_country_data:
        sql_id = "SELECT id FROM videos WHERE tmdb_id =%s AND category= %s"
        values_id = (item["tmdb_id"], item["category"])
        cursor.execute(sql_id, values_id)
        video_id = cursor.fetchall()[0][0]

        production_country_list = item["production_countries"]
        for country in production_country_list:
            sql = "INSERT INTO production_countries (video_id, name) VALUES (%s, %s)"
            values = (video_id, country)
            cursor.execute(sql, values)
            conn.commit()


def saving_provider_data(video_provider_data):
    """Method: Save the data in VideoProvider model"""
    for item in video_provider_data:
        sql_id = "SELECT id FROM videos WHERE tmdb_id =%s AND category= %s"
        values_id = (item["tmdb_id"], item["category"])
        cursor.execute(sql_id, values_id)
        video_id = cursor.fetchall()[0][0]

        provider_list = item["providers"]
        for obj in provider_list:
            sql_provider = f"SELECT id FROM provider WHERE tmdb_id ={obj['provider_id']}"
            cursor.execute(sql_provider)
            provider_id = cursor.fetchall()[0][0]

            sql = "INSERT INTO video_providers (video_id, provider_id,offer_type,link,offer_date,deadline) VALUES (%s,%s,%s,%s,%s,%s)"
            values = (video_id, provider_id, obj["offer_type"], obj["link"], item["crawling_time"], None)
            cursor.execute(sql, values)
            conn.commit()


if __name__ == "__main__":

    """==========DB Connect==========="""

    conn = MySQLdb.connect(
        user=env("DB_USER"),
        passwd=env("DB_PASSWORD"),
        host=env("DB_HOST"),
        port=int(env("DB_PORT")),
        db=env("DB_NAME"),
    )
    cursor = conn.cursor()

    """==========Movie data Saving==========="""
    file_movie_path = "./movieSample.json"

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

    """==========Tv data Saving==========="""

    file_movie_path = "./TvSample.json"

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

    conn.close()
