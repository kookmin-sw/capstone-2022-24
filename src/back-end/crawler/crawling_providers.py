import json

import crawling_sample as cs
import requests


def getMovieProviders(videoData):
    key = videoData["tmdb_id"]
    url = "https://api.themoviedb.org/3/movie/{0}/watch/providers?api_key={1}".format(key, cs.api_key)

    # url 불러오기
    response = requests.get(url)

    # 데이터 값 변환
    contents = response.text
    json_ob = json.loads(contents)

    results = []

    # offer_type_list= list(json_ob['results']['KR'].keys())
    results = {"providers": json_ob["results"]["KR"]}

    """
    offer_type_list.remove('link')

    for item in offer_type_list:
        for iter in json_ob['results']['KR'][item]:
            if str(iter["provider_id"]) in cs.watch_providers:
                result={
                    'offerType': item,
                    'providerid': iter["provider_id"],
                }
                results.append(result)"""

    return results


def getTvProviders(videoData):
    provider = videoData["provider_id"]

    results = []
    for item in provider:
        if videoData["provider_id"] in cs.none_providers_list:
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

    return results
