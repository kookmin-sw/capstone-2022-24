import crawling_sample as cs
import json
import requests
import os
import sys
from datetime import datetime

## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.config.settings")
import django
django.setup()

from web.videos.models import Videos

def getbaseCrawler():
    result = getMoviebaseCrawler()+getTvbaseCrawler()

    return result

def getMoviebaseCrawler():
    result = []
    Movie_dict={}
    Movie_dict= cs.dictMovieUpdate(Movie_dict)
    for key, value in Movie_dict.items():
        url = 'https://api.themoviedb.org/3/movie/{0}?api_key={1}&language={2}'.format(key,cs.api_key,cs.language)

        # url 불러오기
        response = requests.get(url)

        #데이터 값 변환
        contents = response.text
        json_ob = json.loads(contents)

        #date 변환
        date_time_str =json_ob['release_date']
        date_time_obj = datetime.strptime(date_time_str,'%Y-%m-%d').date()

        object = {
            'tmdbid' : value['tmdb_id'],
            'title' : value['title'],
            'releaseDate' : date_time_obj,
            'filmRating' : None,
            'category' : 'MV',
            'posterUrl' : 'https://image.tmdb.org/t/p/original'+ json_ob['poster_path'], #이건.. 크롤링한담에 우리가 저장했다가 따로 써야하니까 일단 임시 데이터 적용
            # 포스터 크기도 고려해야할듯
            'titleEnglish' : json_ob['original_title'],
        }
        result.append(object)

    return result

def getTvbaseCrawler():
    result = []
    Tv_dict={}
    Tv_dict= cs.dictTvUpdate(Tv_dict)
    for key, value in Tv_dict.items():
        url = 'https://api.themoviedb.org/3/tv/{0}?api_key={1}&language={2}'.format(key,cs.api_key,cs.language)

        # url 불러오기
        response = requests.get(url)

        #데이터 값 변환
        contents = response.text
        json_ob = json.loads(contents)

        #date 변환
        date_time_str =json_ob['first_air_date']
        date_time_obj = datetime.strptime(date_time_str,'%Y-%m-%d').date()

        object = {
            'tmdbid' : value['tmdb_id'],
            'title' : value['title'],
            'releaseDate' : date_time_obj,
            'filmRating' : json_ob['adult'],
            'category' : 'TV',
            'posterKey' : 'https://image.tmdb.org/t/p/original'+json_ob['poster_path'],#포스터 크기 고려해야할듯
            'titleEnglish' : json_ob['original_name'],
        }
        result.append(object)

    return result

if __name__ == '__main__':
    videoData = getbaseCrawler()
    print(videoData)
    for item in videoData: #videos Model에 data 저장
        Videos(tmdb_id = item['tmdbid'], title = item['title'], release_date = item['DateField'],
    film_rating= item['filmRating'], category= item['category'], poster_key= item['posterKey'], title_english= item['titleEnglish'] ).save()
