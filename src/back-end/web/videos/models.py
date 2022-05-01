"""Definitions of model about video informations : Video, VideoDetail"""
from django.db import models


class Video(models.Model):
    """Definition of video information that ott providers providered"""

    CATEGORY_CHOICE = (
        ("TV", "TVSeries"),
        ("MV", "Movie"),
    )

    tmdb_id = models.BigIntegerField(
        null=True,
    )
    title = models.CharField(
        max_length=200,
        null=True,
    )
    release_date = models.DateField(
        null=False,
    )
    film_rating = models.CharField(
        max_length=10,
        null=False,
    )
    category = models.CharField(
        max_length=2,
        null=True,
        choices=CATEGORY_CHOICE,
    )
    poster_key = models.ImageField(
        null=True,
    )
    title_english = models.CharField(
        max_length=200,
        null=False,
    )

    class Meta:
        """Metadata for video model"""

        db_table = "videos"

    def __str__(self):
        return f"작품 {self.title}"


class VideoDetail(models.Model):
    """Definition of video detail information that ott providers providered"""

    video_id = models.OneToOneField(
        Video,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    runtime = models.PositiveIntegerField(
        null=False,
    )

    class Meta:
        """Metadata for video details model"""

        db_table = "video_details"

    def __str__(self):
        return f"작품 {self.video.title}의 세부정보"


class Rating(models.Model):
    """Definition about Rating of Video detail Informations"""

    video = models.ForeignKey(
        VideoDetail,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=50,
    )
    value = models.FloatField(
        max_length=10,
    )

    class Meta:
        """Metadata for video ratings model"""

        db_table = "ratings"


class ProductionCountry(models.Model):
    """class to use production_countires arrayfield"""

    video = models.ForeignKey(
        VideoDetail,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=2,
    )

    class Meta:
        """Metadata for video production country model"""

        db_table = "production_countries"


class Gerne(models.Model):
    """Abstract class to use gernes arrayfield"""

    video = models.ForeignKey(
        VideoDetail,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=20,
    )

    class Meta:
        """Metadata for video Gerne model"""

        db_table = "gernes"
