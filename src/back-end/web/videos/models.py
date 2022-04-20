"""Videos App Model Definitions: Video, VideoDetail"""
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
