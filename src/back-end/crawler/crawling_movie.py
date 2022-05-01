import json
from datetime import datetime

import requests

watch_providers = ["8", "337", "356", "97", "119"]
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
        total_pages = 1

        # dict 제작
        for i in range(1, total_pages + 1):
            if i <= 500:
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
                    if checkSample(id) == True:
                        break
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
                    if checkSample(id) == True:
                        break
                    title = json_obj["results"][j]["title"]
                    Movie_dict[id] = {"tmdb_id": id, "title": title, "Category": "Movie"}
        break
    return Movie_dict


def checkSample(id):  # 이미 Movie 데이터가 있는지 check 하는 용도
    file_path = "./Moviesample.json"
    with open(file_path, "r") as infile:  # open 해서 데이터 확인 할것임
        Sample_data = json.load(infile)
        Sample_data = json.dumps(Sample_data)
    if str(id) in Sample_data:  # 이미 데이터가 있음
        return True
    else:  # 데이터 없음
        return False


def getMovieData():
    results = {}
    Movie_dict = {}
    Movie_dict = dictMovieUpdate(Movie_dict)
    for key, value in Movie_dict.items():
        Movie = []

        # Crawling time 기록
        now = datetime.now()
        time = {"CralingTime": now.strftime("%Y-%m-%d %H:%M:%S")}
        Movie.append(time)

        # base, detail 정보 Crawler
        url = "https://api.themoviedb.org/3/movie/{0}?api_key={1}&language={2}".format(key, api_key, language)
        response = requests.get(url)

        # 데이터 값 변환
        contents = response.text
        json_ob = json.loads(contents)
        Movie.append(json_ob)

        # provider 정보 Crawler
        url = "https://api.themoviedb.org/3/movie/{0}/watch/providers?api_key={1}".format(key, api_key)
        response = requests.get(url)

        # 데이터 값 변환
        contents = response.text
        json_ob = json.loads(contents)
        providers = {"providers": json_ob["results"]["KR"]}
        Movie.append(providers)

        # casts 정보 Crawler
        url = "https://api.themoviedb.org/3/movie/{0}/credits?api_key={1}&language={2}".format(key, api_key, language)
        response = requests.get(url)

        # 데이터 값 변환
        contents = response.text
        json_ob = json.loads(contents)
        casts = {"casts": json_ob["cast"]}
        Movie.append(casts)

        results[key] = {"data": Movie}

    return results


file_path = "./MovieSample.json"
videoData = getMovieData()
with open(file_path, "w") as outfile:
    json.dump(videoData, outfile)