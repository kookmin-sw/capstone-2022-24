import json

import requests

watch_providers = ["8", "337", "356", "97", "119"]  # 순서대로 넷플, 디플, 웨이브, 왓챠, 아마존 프라임 ID
none_providers_list = ["356"]  # 검색에 문제있는 리스트 (여기서는 웨이브)
api_key = ""
language = "ko-KR"
watch_region = "KR"


def dictMovieUpdate(Movie_dict):
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
        total_pages = 1  # 테스트 조절을 위해 페이지수 제한

        # dict 제작
        for i in range(1, total_pages + 1):
            if i <= 500:  # page가 분명 1000까지 허용이라는데 왜 500넘으면 오류가 뜨냐고
                page_Num = i
                Url = "https://api.themoviedb.org/3/discover/movie?api_key={0}&language={1}&sort_by=popularity.desc&certification_country=KR&page={2}&with_watch_providers={3}&watch_region={4}".format(
                    api_key, language, page_Num, provider, watch_region
                )
                rsp = requests.get(Url)
                content = rsp.text
                json_obj = json.loads(content)
                count = len(json_obj["results"])
                for j in range(count):
                    id = json_obj["results"][j]["id"]
                    title = json_obj["results"][j]["title"]
                    Movie_dict[id] = {"tmdb_id": id, "title": title, "Category": "Movie"}
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
                    title = json_obj["results"][j]["title"]
                    Movie_dict[id] = {"tmdb_id": id, "title": title, "Category": "Movie"}
    return Movie_dict


def dictTvUpdate(Tv_dict):
    for provider in watch_providers:
        url = "https://api.themoviedb.org/3/discover/tv?api_key={0}&language={1}&sort_by=popularity.desc&page={2}&with_watch_providers={3}&watch_region={4}".format(
            api_key, language, 1, provider, watch_region
        )

        # url 불러오기
        response = requests.get(url)

        # 데이터 값 변환
        contents = response.text
        json_ob = json.loads(contents)
        total_pages = json_ob["total_pages"]
        total_pages = 1  # 테스트 조절을 위해 페이지수 제한

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
                    title = json_obj["results"][j]["name"]
                    if id in Tv_dict:
                        list = Tv_dict[id]["provider_id"]
                    else:
                        list = []
                    list.append(provider)
                    Tv_dict[id] = {"tmdb_id": id, "title": title, "Category": "TV", "provider_id": list}
            else:
                page_Num = i - 500
                Url = "https://api.themoviedb.org/3/discover/tv?api_key={0}&language={1}&sort_by=popularity.desc&page={2}&with_watch_providers={3}&watch_region={4}".format(
                    api_key, language, page_Num, provider, watch_region
                )
                rsp = requests.get(Url)
                content = rsp.text
                json_obj = json.loads(content)
                count = len(json_obj["results"])
                for j in range(count):
                    id = json_obj["results"][j]["id"]
                    title = json_obj["results"][j]["name"]
                    if id in Tv_dict:
                        list = Tv_dict[id]["provider_id"]
                    else:
                        list = []
                    list.append(provider)
                    Tv_dict[id] = {"tmdb_id": id, "title": title, "Category": "TV", "provider_id": list}

    return Tv_dict


def dictVideoUpdate(Movie_dict, Tv_dict):
    print(len(dictMovieUpdate(Movie_dict)) + len(dictTvUpdate(Tv_dict)))
    videos_dict = {"Movies": Movie_dict, "Tv Series": Tv_dict}

    return videos_dict


Tv_dict = {}
Movie_dict = {}
dictVideoUpdate(Movie_dict, Tv_dict)
