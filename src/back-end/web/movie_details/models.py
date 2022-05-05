"""Definitions of model about movie detail informations : MovieDetails"""
from django.db import models
from videos.models import Video


class MovieDetail(models.Model):
    """Definition of detailed information about Movie among the video category"""

    video = models.OneToOneField(
        Video,
        on_delete=models.CASCADE,
    )
    overview = models.TextField(
        null=True,
    )
    trailer_key = models.URLField(
        max_length=150,
        null=True,
    )
    source = models.CharField(
        max_length=50,
        null=True,
    )

    class Meta:
        """Metadata for movie details model"""

        db_table = "movie_details"
