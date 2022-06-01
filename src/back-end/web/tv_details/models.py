"""Definitions of model about tv detail informations : TvSeriesDetail, TvSeason, TvSeasonDetail"""
from django.db import models
from videos.models import Video


class TvSeriesDetail(models.Model):
    """Definition of detailed information about Tv Series among the video category"""

    video = models.OneToOneField(
        Video,
        on_delete=models.CASCADE,
    )
    number_of_seasons = models.PositiveIntegerField(
        default=1,
    )
    number_of_episodes = models.PositiveIntegerField(
        default=1,
    )
    trailer_key = models.URLField(
        max_length=100,
        null=True,
    )

    class Meta:
        """Metadata for Tv Series details model"""

        db_table = "tv_series_details"


class TvSeason(models.Model):
    """Definition of list about TV seasons that compose the TV series"""

    series = models.ForeignKey(
        TvSeriesDetail,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        null=True,
        max_length=50,
    )
    number = models.PositiveIntegerField()

    class Meta:
        """Metadata for Tv Season model"""

        db_table = "tv_seasons"


class TvSeasonDetail(models.Model):
    """Definition of detailed information about TV seasons that compose the TV series"""

    series = models.ForeignKey(
        TvSeriesDetail,
        on_delete=models.CASCADE,
    )
    number_of_total_episodes = models.PositiveIntegerField(
        null=True,
    )
    number = models.PositiveIntegerField(
        default=0,
    )
    overview = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        """Metadata for Tv season details model"""

        db_table = "tv_season_details"
