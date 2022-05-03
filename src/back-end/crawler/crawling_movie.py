"""Craling Movie Data from TMDB"""
from datetime import datetime

from crawler_base import *


def dict_movie_update(data_path):
    Movie_dict = {}
    for provider in watch_providers:
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language={language}&sort_by=popularity.desc&certification_country=KR&page=1&with_watch_providers={provider}&watch_region={watch_region}"

        json_ob = get_request_to_object(url)
        total_pages = json_ob["total_pages"]

        for i in range(1, total_pages + 1):
            if i <= 500:
                page_num = i
                url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language={language}&sort_by=popularity.desc&certification_country=KR&page={page_num}&with_watch_providers={provider}&watch_region={watch_region}"
                json_obj = get_request_to_object(url)
                count = len(json_obj["results"])
                for j in range(count):
                    id = json_obj["results"][j]["id"]
                    if check_sample(id, data_path) == True:
                        break
                    title = json_obj["results"][j]["title"]
                    Movie_dict[id] = {"tmdb_id": id, "title": title, "Category": "Movie"}
            else:
                page_num = i - 500
                url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language={language}&sort_by=popularity.desc&certification_country=KR&page={page_num}&with_watch_providers={provider}&watch_region={watch_region}"
                json_obj = get_request_to_object(url)
                count = len(json_obj["results"])
                for j in range(count):
                    id = json_obj["results"][j]["id"]
                    if check_sample(id, data_path) == True:
                        break
                    title = json_obj["results"][j]["title"]
                    Movie_dict[id] = {"tmdb_id": id, "title": title, "Category": "Movie"}

    return Movie_dict


def get_movie_data(file_path):
    results = {}
    Movie_dict = dict_movie_update(file_path)
    for key, value in Movie_dict.items():
        Movie = []

        """Record crawling time"""
        now = datetime.now()
        time = {"craling_time": now.strftime("%Y-%m-%d %H:%M:%S")}
        Movie.append(time)

        """video base, details Crawler"""
        url = "https://api.themoviedb.org/3/movie/{0}?api_key={1}&language={2}".format(key, api_key, language)
        json_ob = get_request_to_object(url)
        Movie.append(json_ob)

        """provider Classification"""
        url = "https://api.themoviedb.org/3/movie/{0}/watch/providers?api_key={1}".format(key, api_key)
        json_ob = get_request_to_object(url)
        providers = {"providers": json_ob["results"]["KR"]}
        Movie.append(providers)

        """
        casts Crawling : Comment it because there're no plans to use it yet.
        url = "https://api.themoviedb.org/3/movie/{0}/credits?api_key={1}&language={2}".format(key, api_key, language)
        json_ob = get_request_to_object(url)
        casts = {"casts": json_ob["cast"]}
        Movie.append(casts)
        """

        results[key] = {"data": Movie}

    return results
