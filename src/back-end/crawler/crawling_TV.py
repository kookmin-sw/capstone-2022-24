"""Craling TV Data to TMDB"""
import json
from datetime import datetime

import requests
from crawler_base import *


def dictTvUpdate(data_path):
    Tv_dict = {}
    for provider in watch_providers:
        url = "https://api.themoviedb.org/3/discover/movie?api_key={0}&language={1}&sort_by=popularity.desc&certification_country=KR&page={2}&with_watch_providers={3}&watch_region={4}".format(
            api_key, language, 1, provider, watch_region
        )

        # url 불러오기
        response = requests.get(url)

        # 데이터 값 변환
        contents = response.text
        json_ob = json.loads(contents)
        total_pages = json_ob["total_pages"]

        # dict 제작
        for i in range(1, total_pages + 1):
            if i <= 500:
                page_Num = i
                Url = "https://api.themoviedb.org/3/discover/tv?api_key={0}&language={1}&sort_by=popularity.desc&page={2}&with_watch_providers={3}&watch_region={4}".format(
                    api_key, language, page_Num, provider, watch_region
                )
                rsp = requests.get(Url)
                content = rsp.text
                json_obj = json.loads(content)
                count = len(json_obj["results"])
                for j in range(count):
                    id = json_obj["results"][j]["id"]
                    if checkSample(id, data_path) == True:
                        break
                    if id in Tv_dict:
                        list = Tv_dict[id]["provider_id"]
                    else:
                        list = []
                    list.append(provider)
                    title = json_obj["results"][j]["name"]
                    Tv_dict[id] = {"tmdb_id": id, "title": title, "Category": "TV", "provider_id": list}
            else:
                page_Num = i - 500
                Url = "https://api.themoviedb.org/3/discover/movie?api_key={0}&language={1}&sort_by=popularity.asc&certification_country=KR&page={2}&with_watch_providers={3}&watch_region={4}".format(
                    api_key, language, page_Num, provider, watch_region
                )
                rsp = requests.get(Url)
                content = rsp.text
                json_obj = json.loads(content)
                count = len(json_obj["results"])
                for j in range(count):
                    id = json_obj["results"][j]["id"]
                    if checkSample(id, data_path) == True:
                        break
                    if id in Tv_dict:
                        list = Tv_dict[id]["provider_id"]
                    else:
                        list = []
                    list.append(provider)
                    title = json_obj["results"][j]["name"]
                    Tv_dict[id] = {"tmdb_id": id, "title": title, "Category": "TV", "provider_id": list}

    return Tv_dict


def getTvData(file_path):
    results = {}
    Tv_dict = dictTvUpdate(file_path)
    for key, value in Tv_dict.items():
        TV = []

        # Crawling time 기록
        now = datetime.now()
        time = {"CralingTime": now.strftime("%Y-%m-%d %H:%M:%S")}
        TV.append(time)

        # base, detail 정보 Crawler
        url = "https://api.themoviedb.org/3/tv/{0}?api_key={1}&language={2}".format(key, api_key, language)
        response = requests.get(url)

        # 데이터 값 변환
        contents = response.text
        json_ob = json.loads(contents)
        TV.append(json_ob)

        provider = value["provider_id"]

        results = []
        for item in provider:
            if value["provider_id"] in none_providers_list:
                result = {
                    "offerType": None,
                    "providerid": item["provider_id"],
                }
            else:
                result = {
                    "offerType": "flatrate",
                    "providerid": item["provider_id"],
                }
            results.append(result)

        """# casts 정보 Crawler
        url = "https://api.themoviedb.org/3/movie/{0}/credits?api_key={1}&language={2}".format(key, api_key, language)
        response = requests.get(url)

        # 데이터 값 변환
        contents = response.text
        json_ob = json.loads(contents)
        casts = {"casts": json_ob["cast"]}
        TV.append(casts)"""

        results[key] = {"data": TV}

    return results
