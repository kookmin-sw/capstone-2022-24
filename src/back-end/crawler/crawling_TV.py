"""Craling TV Data to TMDB"""
from datetime import datetime

from crawler_base import *


def dict_tv_update(data_path):
    """Method: checking the already had tv dict and updating it"""

    Tv_dict = {}
    for provider in watch_providers:
        check_url = f"https://api.themoviedb.org/3/discover/tv?api_key={api_key}&language={language}&sort_by=popularity.desc&page=1&with_watch_providers={provider}&watch_region={watch_region}"

        json_ob = get_request_to_object(check_url)
        total_pages = json_ob["total_pages"]

        for i in range(1, total_pages + 1):
            if i <= MAX_PAGE_LIMIT:
                page_Num = i
                url = f"https://api.themoviedb.org/3/discover/tv?api_key={api_key}&language={language}&sort_by=popularity.desc&page={page_Num}&with_watch_providers={provider}&watch_region={watch_region}"

                json_obj = get_request_to_object(url)
                count = len(json_obj["results"])
                for j in range(count):
                    id = json_obj["results"][j]["id"]
                    if check_sample(id, data_path) == True:
                        break
                    if id in Tv_dict:
                        list = Tv_dict[id]["provider_id"]
                    else:
                        list = []
                    list.append(provider)
                    title = json_obj["results"][j]["name"]
                    Tv_dict[id] = {"tmdb_id": id, "title": title, "Category": "TV", "provider_id": list}
            else:
                page_Num = i - MAX_PAGE_LIMIT
                url = f"https://api.themoviedb.org/3/discover/tv?api_key={api_key}&language={language}&sort_by=popularity.desc&page={page_Num}&with_watch_providers={provider}&watch_region={watch_region}"

                json_obj = get_request_to_object(url)
                count = len(json_obj["results"])

                for j in range(count):
                    id = json_obj["results"][j]["id"]
                    if check_sample(id, data_path) == True:
                        break
                    if id in Tv_dict:
                        list = Tv_dict[id]["provider_id"]
                    else:
                        list = []
                    list.append(provider)
                    title = json_obj["results"][j]["name"]
                    Tv_dict[id] = {"tmdb_id": id, "title": title, "Category": "TV", "provider_id": list}

    return Tv_dict


def get_tv_data(file_path):
    """Method: Creating a tv data Using tv dict"""

    results = {}
    Tv_dict = dict_tv_update(file_path)
    for key, value in Tv_dict.items():
        TV = []

        """Record crawling time"""
        now = datetime.now()
        time = {"crawling_time": now.strftime("%Y-%m-%d %H:%M:%S")}
        TV.append(time)

        """video base, details Crawler"""
        url = f"https://api.themoviedb.org/3/tv/{key}?api_key={api_key}&language={language}"

        json_ob = get_request_to_object(url)
        TV.append(json_ob)

        """provider Classification"""
        provider = value["provider_id"]

        provider_list = []
        for item in provider:
            if item in none_providers_list:
                obj = {
                    "offer_type": None,
                    "provider_id": item,
                }
            else:
                obj = {
                    "offer_type": "flatrate",
                    "provider_id": item,
                }
            provider_list.append(obj)

        provider_obj = {"provider": provider_list}
        TV.append(provider_obj)

        """video english title Crawler"""
        url = f"https://api.themoviedb.org/3/tv/{key}?api_key={api_key}&language=en-US"
        json_ob = get_request_to_object(url)
        title_english = check_vaild(json_ob, "name")
        object_en_title = {"title_english": title_english}
        TV.append(object_en_title)

        """video film rating Crawler"""
        url = f"https://api.themoviedb.org/3/tv/{key}/content_ratings?api_key={api_key}&language=en-US"
        json_ob = get_request_to_object(url)
        TV.append(json_ob)

        """
        casts Crawling : Comment it because there're no plans to use it yet.
        url =  f"https://api.themoviedb.org/3/tv/{key}/credits?api_key={api_key}&language={language}"
        json_ob = get_request_to_object(url)
        casts = {"casts": json_ob["cast"], "crews": json_ob["crew"]}
        TV.append(casts)
        """
        results[key] = {"data": TV}

    return results


if __name__ == "__main__":

    tv_data_path = "./TvSample.json"
    tv_data = get_tv_data(tv_data_path)
    with open(tv_data_path, "w") as outfile:
        json.dump(tv_data, outfile)
