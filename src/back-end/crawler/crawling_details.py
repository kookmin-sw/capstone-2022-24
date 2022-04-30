import json

import crawling_base as bs
import crawling_providers as cp
import crawling_sample as cs
import requests


def getVideodetails(videoData):
    videoDetailData = []
    for i in range(len(videoData)):
        if videoData[i]["category"] == "MV":
            videoDetailData.append(getMoveidetails(videoData[i]))
        elif videoData[i]["category"] == "TV":
            videoDetailData.append(getTvdetails(videoData[i]))
    return videoDetailData


def getMoveidetails(videoData):
    key = videoData["tmdbid"]
    url = "https://api.themoviedb.org/3/movie/{0}?api_key={1}&language={2}".format(key, cs.api_key, cs.language)

    # url 불러오기
    response = requests.get(url)

    # 데이터 값 변환
    contents = response.text
    json_ob = json.loads(contents)

    genres_list = []
    for item in json_ob["genres"]:
        genres_list.append(item["name"])

    production_list = []
    for item in json_ob["production_countries"]:
        production_list.append(item["iso_3166_1"])

    providers = cp.getMovieProviders(videoData)
    result = {
        "category": "MV",
        "tmbdid": key,
        "runtime": json_ob["runtime"],  # 분 단위로 들어감
        "rating": 0,  # 임시 처리
        "produtionCountry": production_list,
        "gernes": genres_list,
        "providers": providers,
    }
    return result


def getTvdetails(videoData):
    key = videoData["tmdbid"]
    url = "https://api.themoviedb.org/3/tv/{0}?api_key={1}&language={2}".format(key, cs.api_key, cs.language)

    # url 불러오기
    response = requests.get(url)

    # 데이터 값 변환
    contents = response.text
    json_ob = json.loads(contents)

    genres_list = []
    for item in json_ob["genres"]:
        genres_list.append(item["name"])

    production_list = []
    for item in json_ob["production_countries"]:
        production_list.append(item["iso_3166_1"])

    providers = cp.getTVProviders(videoData)

    result = {
        "category": "TV",
        "tmbdid": key,
        "runtime": None,
        "rating": 0,  # 임시 처리
        "produtionCountry": production_list,
        "gernes": genres_list,
        "providers": providers,
    }
    return result


providerlink_dict = {
    "8": "https://www.netflix.com/kr/",
    "356": "https://www.wavve.com/",
    "97": "https://watcha.com/",
    "337": "https://www.disneyplus.com/ko-kr",
}

if __name__ == "__main__":
    videoData = bs.getbaseCrawler()
    videoDetailData = getVideodetails(videoData)
    print(videoDetailData)
