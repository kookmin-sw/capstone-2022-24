from unicodedata import category
import crawling_base as bs
import crawling_sample as cs
import json
import requests
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.config.settings")
import django
django.setup()

from web.videos.models import video_details

def getVideodetails(videoData):    
    for i in range(len(videoData)):
        if videoData[i][category]=='Movie':
            videoDetailData.append(getMoveidetails(videoData[i]))
        elif videoData[i][category]=='Tv':
            videoDetailData.append(getTvdetails(videoData[i]))

def getMoveidetails(videoData):
    key= videoData['tmdb_id']
    url = 'https://api.themoviedb.org/3/movie/{0}?api_key={1}&language={2}'.format(key,cs.api_key, cs.language)
        
    # url 불러오기
    response = requests.get(url)

    #데이터 값 변환
    contents = response.text
    json_ob = json.loads(contents)
    
    result = {
        'runtime' : videoData['runtime'],
        'rating' : 0, #임시 처리
        'produtionCountry' : json_ob['production_countries'][0]['iso_3166_1'], #일단 첫 나라만 따오게 했는데 list화 할지 고려해보기로
        'gernes' : json_ob['genres'], #list 구조
    }
    return result

def getTvdetails(videoData):
    key= videoData['tmdb_id']
    url = 'https://api.themoviedb.org/3/tv/{0}?api_key={1}&language={2}'.format(key,cs.api_key,cs.language)
        
    # url 불러오기
    response = requests.get(url)

    #데이터 값 변환
    contents = response.text
    json_ob = json.loads(contents)
        
    result = {
        'runtime' : None,
        'rating' : 0, #임시 처리
        'produtionCountry' : json_ob['production_countries'][0]['iso_3166_1'], 
        'gernes' : json_ob['genres'],
    }
    return result

if __name__ == '__main__':
    videoData = bs.getbaseCrawler() #원래 DB에서 정보 따와서 하는게 좋을거 같은데 임시용 설정
    videoDetailData= getVideodetails(videoData)
    for item in videoDetailData:
        video_details(runtime= item['runtime'], rating=item['runtime'], productionCountry= item['productionCountry'], gernes= item['gernes'])