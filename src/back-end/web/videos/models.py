#from platform import release
#from unicodedata import category
from djongo import models
import json

# Create your models here.
class videos(models.Model):
    categories = (
        ("Tv", "TvSeries"), # 앞= DB에 표시되는값 뒤= admin이나 form에 연결되는 값
        ("Movie", "Movie"), # 위와 동일
    )
    tmdbid = models.IntegerField(null=True)
    title = models.CharField(max_length=200,null=True)
    releaseDate = models.DateField(null=False)
    filmRating = models.CharField(max_length=10,null=False) 
    category = models.CharField(max_length=5,null=True, choices=categories) #choices 로 categories와 연결됨.
    posterKey = models.CharField(max_length=100,null=False)
    titleEnglish = models.CharField(max_length=200,null=False)
    

class video_details(models.Model):
    videoId= models.ForeignKey(videos, on_delete=models.CASCADE) #연결된 video객체 삭제시 같이 삭제
    runtime = models.IntegerField(null=False)
    rating = models.ArrayField(null=False) #이걸 확장가능성 있게 코딩해야할까? => array 분리
    productionCountry= models.CharField(null=False)
    gernes= models.ArrayField(null=True) #빈 리스트일순 있어도 Null일순 없는 구조로 생각함.

#SQL 용어로 DB정규화 문제
#작은 서버에선 구조가 더 중요해서...
#하나의 데이터로 가져가지 않고 string으로 가져가고 묶어서 가는게 보통 큰 서버임
# ㄴ> 데이터로 하나씩 뺄수도 있고 반대로 할수도 있고...
# ㄴ> 이건 종고 반영해서 수정하면 될거같음...
