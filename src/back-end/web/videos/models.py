"""Videos App Model Definitions: Video, VideoDetail"""
from django import forms
from djongo import models


class Video(models.Model):
    """Video information that ott providers support"""

    CATEGORY_CHOICE = (
        ("TV", "TVSeries"),
        ("MV", "Movie"),
    )

    id = models.BigAutoField(
        primary_key=True,
    )
    tmdb_id = models.BigIntegerField(
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
        max_length=2,
        null=True,
        choices=CATEGORY_CHOICE,
    )
    poster_key = models.ImageField(
        db_column="posterKey",
    )
    title_english = models.CharField(
        max_length=200,
        null=False,
        db_column="titleEnglish",
    )

    class Meta:
        """DB table naming"""

        db_table = "videos"

    def __str__(self):
        return f"{self.title}"


class Rating(models.Model):
    """Abstract class to use ratings arrayfield"""

    name = models.CharField(
        max_length=50,
    )
    value = models.FloatField(
        max_length=10,
    )
    objects = models.DjongoManager()

    class Meta:
        """type setting"""

        abstract = True

class ProductionCountry(models.Model):
    """Abstract class to use production_countires arrayfield"""

    name = models.CharField(max_length=2)
    objects = models.DjongoManager()

    class Meta:
        """type setting"""

        abstract = True


class Gerne(models.Model):
    """Abstract class to use gernes arrayfield"""

    name = models.CharField(max_length=20)
    objects = models.DjongoManager()

    class Meta:
        """type setting"""

        abstract = True


class VideoDetail(models.Model):
    """videoDetails models"""

    id = models.BigAutoField(
        primary_key=True,
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        db_column="videoId",
    )
    runtime = models.IntegerField(
        null=False,
    )
    ratings = models.ArrayField(
        model_container=Rating,
        null=False,
    )
    production_countries = models.ArrayField(
        model_container=ProductionCountry,
        null=False,
        db_column="productionCountries",
    )
    gernes = models.ArrayField(
        model_container=Gerne,
        max_length=50,
        null=True,
    )

    class Meta:
        """DB table naming"""

        db_table = "video_details"

    def __str__(self):
        return f"{self.video.title}의 세부정보"

