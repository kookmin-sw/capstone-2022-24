import requests
import laftel


api_key = '6801LRG1BBD83081NF89'

print(laftel.sync.getAnimeInfo(39986))
#이걸로 얻어올수 있는 라프텔 정보 = 제목, 라프텔 작품 id, 라프텔 링크, 이미지 링크, 줄거리, 상영등급, 장르, 개봉시기(날짜X, 연도/분기 개념), 방송일
# #ERD에서 없는 정보: 영어이름, 제작국가

from urllib.parse import quote

import requests

laftel_API = ' https://laftel.net/api/v1.0/items/39986/detail/'

header = {'laftel' : 'TeJava'}
response = requests.get(url = laftel_API, headers = header)
print(response.text)

#제작진 정보는 작가, 그림(만화인듯..?), 제작회사 정도
