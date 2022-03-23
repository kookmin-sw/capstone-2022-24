import json
import requests
import datetime

watch_providers = ['8','337', '356', '97'] #순서대로 넷플, 디플, 웨이브, 왓챠 ID
api_key= '12f96752972cb21d06643a3fc2a311bd'
language='ko-KR'
watch_region= 'KR'

def dictMovieUpdate(Movie_dict):
    for provider in watch_providers:
        url = 'https://api.themoviedb.org/3/discover/movie?api_key={0}&language={1}&sort_by=popularity.desc&certification_country=KR&page={2}&with_watch_providers={3}&watch_region={4}'.format(api_key,language,1,provider,watch_region)

        # url 불러오기
        response = requests.get(url)

        #데이터 값 변환
        contents = response.text
        json_ob = json.loads(contents)
        total_pages = json_ob['total_pages']
        total_pages = 1 #테스트 조절을 위해 페이지수 제한

        #dict 제작
        for i in range(1, total_pages+1):
            if i<=500: #page가 분명 1000까지 허용이라는데 왜 500넘으면 오류가 뜨냐고
                page_Num= i
                Url = 'https://api.themoviedb.org/3/discover/movie?api_key={0}&language={1}&sort_by=popularity.desc&certification_country=KR&page={2}&with_watch_providers={3}&watch_region={4}'.format(api_key,language,page_Num,provider,watch_region)
                rsp = requests.get(Url)
                content = rsp.text
                json_obj = json.loads(content)
                count = len(json_obj['results'])
                for j in range(count):
                    id = json_obj['results'][j]['id']
                    title = json_obj['results'][j]['title']
                    Movie_dict[id]= {'tmdb_id': id, 'title': title, 'Category': 'Movie'}
            else:
                page_Num= i-500
                Url = 'https://api.themoviedb.org/3/discover/movie?api_key={0}&language={1}&sort_by=popularity.asc&certification_country=KR&page={2}&with_watch_providers={3}&watch_region={4}'.format(api_key,language,page_Num,provider,watch_region)
                rsp = requests.get(Url)
                content = rsp.text
                json_obj = json.loads(content)
                count = len(json_obj['results'])
                for j in range(count):
                    id = json_obj['results'][j]['id']
                    title = json_obj['results'][j]['title']
                    Movie_dict[id]= {'tmdb_id': id, 'title': title, 'Category': 'Movie'}

    return Movie_dict
    
def dictTvUpdate(Tv_dict):
    for provider in watch_providers:
        url= 'https://api.themoviedb.org/3/discover/tv?api_key={0}&language={1}&sort_by=popularity.desc&page={2}&with_watch_providers={3}&watch_region={4}'.format(api_key,language,1,provider,watch_region)

        # url 불러오기
        response = requests.get(url)

        #데이터 값 변환
        contents = response.text
        json_ob = json.loads(contents)
        total_pages = json_ob['total_pages']
        total_pages = 1 #테스트 조절을 위해 페이지수 제한
        
        for i in range(1, total_pages+1):
            if i<=500:
                page_Num= i
                Url = 'https://api.themoviedb.org/3/discover/tv?api_key={0}&language={1}&sort_by=popularity.desc&page={2}&with_watch_providers={3}&watch_region={4}'.format(api_key,language,page_Num,provider,watch_region)
                rsp = requests.get(Url)
                content = rsp.text
                json_obj = json.loads(content)
                count = len(json_obj['results'])
                for j in range(count):
                    id = json_obj['results'][j]['id']
                    title = json_obj['results'][j]['name']
                    Tv_dict[id]= {'tmdb_id': id, 'title': title, 'Category': 'TV'}
            else:
                page_Num= i-500
                Url = 'https://api.themoviedb.org/3/discover/tv?api_key={0}&language={1}&sort_by=popularity.desc&page={2}&with_watch_providers={3}&watch_region={4}'.format(api_key,language,page_Num,provider,watch_region)
                rsp = requests.get(Url)
                content = rsp.text
                json_obj = json.loads(content)
                count = len(json_obj['results'])
                for j in range(count):
                    id = json_obj['results'][j]['id']
                    title = json_obj['results'][j]['name']
                    Tv_dict[id]= {'tmdb_id': id, 'title': title, 'Category': 'TV'}
    
    return Tv_dict
    
def dictVideoUpdate(Movie_dict,Tv_dict):
    dictMovieUpdate(Movie_dict)
    dictTvUpdate(Tv_dict)
    videos_dict={'Movies': Movie_dict, 'Tv Series': Tv_dict}

    return videos_dict

