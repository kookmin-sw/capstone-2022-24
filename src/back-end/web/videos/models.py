from djongo import models

class Videos(models.Model):
    CATEGORY_CHOICE = (
        ("TV", "TVSeries"), # 앞= DB에 표시되는값 뒤= admin이나 form에 연결되는 값
        ("MV", "Movie"), # 위와 동일
    )


    id= models.BigAutoField(
        primary_key=True,
    )
    tmdb_id = models.IntegerField(
        null=True,
        db_column="tmdbId",
    )
    title = models.CharField(
        max_length=200,
        null=True,
    )
    release_date = models.DateField(
        null=False,
        db_column="releaseDate",
    )
    film_rating = models.CharField(
        max_length=10,
        null=False,
        db_column="filmRating",
    )
    category = models.CharField(
        max_length = 2,
        null = True,
        choices=CATEGORY_CHOICE,
    )
    poster_key = models.ImageField(
        db_column="posterKey",
    )
    title_english = models.CharField(
        max_length=200,
        null=False,
        db_column="baseDate",
    )

    class Meta:
        db_table = "videos"

    def __str__(self):
        return f"{self.name}"



class VideoDetails(models.Model):
    COUNTRY_CHOICE=(
        ('KR','국내'),
        ('Other','국외'),
        (), #하 예시 존나 많아....서 일단 이 버전으로 만들어둠
    )

    id= models.BigAutoField(
        primary_key=True,
    )
    video_id= models.ForeignKey(
        Videos,
        on_delete=models.CASCADE, #연결된 video객체 삭제시 같이 삭제
        db_column="videoId",
    )
    runtime = models.IntegerField(
        null=False,
    )
    rating = models.ArrayField(
        null=False,
    )
    production_country= models.CharField(
        max_length=2,
        null=False,
        choices=COUNTRY_CHOICE,
        db_column="productionCountry",
    )
    gernes= models.ArrayField(
        max_length=50,
        null=True,
    )

    class Meta:
        db_table = "video_details"

    def __str__(self):
        return f"{self.name}"
