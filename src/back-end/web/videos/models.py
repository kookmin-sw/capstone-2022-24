from djongo import models

# Create your models here.
class videos(models.Model):
    _id= models.ObjectIdField()
    categories = (
        ("Tv", "TvSeries"), # 앞= DB에 표시되는값 뒤= admin이나 form에 연결되는 값
        ("Movie", "Movie"), # 위와 동일
    )
    tmdbid = models.IntegerField(null=True)
    title = models.CharField(max_length=200,null=True)
    releaseDate = models.DateField(null=False)
    filmRating = models.CharField(max_length=10, null=False) 
    category = models.CharField(max_length=5, null=True, choices=categories) #choices 로 categories와 연결됨.
    posterKey = models.CharField(max_length=100,null=False)
    titleEnglish = models.CharField(max_length=200,null=False)
    

class video_details(models.Model):
    _id= models.ObjectIdField()
    videoId= models.ForeignKey(videos, on_delete=models.CASCADE) #연결된 video객체 삭제시 같이 삭제
    runtime = models.IntegerField(null=False)
    rating = models.ArrayField(null=False) #이걸 확장가능성 있게 코딩해야할까? => array 분리
    productionCountry= models.CharField(max_length=100, null=False)
    gernes= models.ArrayField(max_length=50, null=True) #빈 리스트일순 있어도 Null일순 없는 구조로 생각함.
