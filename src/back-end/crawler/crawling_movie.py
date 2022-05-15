"""Crawling Movie Data using API data"""
from datetime import datetime

from crawler_base import *


def dict_movie_update(data_path):
    """Method: checking the already had Movie dict and updating it"""

    Movie_dict = {}
    for provider in watch_providers:
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language={language}&sort_by=popularity.desc&certification_country=KR&page=1&with_watch_providers={provider}&watch_region={watch_region}"

        json_ob = get_request_to_object(url)
        total_pages = json_ob["total_pages"]

        for i in range(1, total_pages + 1):
            if i <= MAX_PAGE_LIMIT:
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
                page_num = i - MAX_PAGE_LIMIT
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
    """Method: Creating a movie data Using movie dict"""

    results = {}
    Movie_dict = dict_movie_update(file_path)
    for key, value in Movie_dict.items():
        Movie = []

        """Record crawling time"""
        now = datetime.now()
        time = {"crawling_time": now.strftime("%Y-%m-%d %H:%M:%S")}
        Movie.append(time)

        """video base, details Crawler"""
        url = f"https://api.themoviedb.org/3/movie/{key}?api_key={api_key}&language={language}"
        json_ob = get_request_to_object(url)
        Movie.append(json_ob)

        """video providers Crawler"""
        url = f"https://api.themoviedb.org/3/movie/{key}/watch/providers?api_key={api_key}"
        json_ob = get_request_to_object(url)
        try:
            providers = {"providers": json_ob["results"]["KR"]}
        except:
            continue
        Movie.append(providers)

        """video english title Crawler"""
        url = f"https://api.themoviedb.org/3/movie/{key}?api_key={api_key}&language=en-US"
        json_ob = get_request_to_object(url)
        title_english = check_vaild(json_ob, "title")
        object_en_title = {"title_english": title_english}
        Movie.append(object_en_title)

        """
        casts Crawling : Comment it because there're no plans to use it yet.
        url = f"https://api.themoviedb.org/3/movie/{key}/credits?api_key={api_key}&language={language}"
        json_ob = get_request_to_object(url)
        casts = {"casts": json_ob["cast"]}
        Movie.append(casts)
        """

        results[key] = {"data": Movie}

    return results


if __name__ == "__main__":
    movie_data_path = "./movieSample.json"
    movie_data = get_movie_data(movie_data_path)
    with open(movie_data_path, "w") as outfile:
        json.dump(movie_data, outfile)
