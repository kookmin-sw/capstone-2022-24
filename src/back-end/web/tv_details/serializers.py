"""Serializers of tv details application for json parsing : TvSeriesDetailSerializer, TvSeasonSerializer,
                                                            TvSeasonDetailSerializer"""
from rest_framework import serializers
from tv_details.models import TvSeason, TvSeasonDetail, TvSeriesDetail
from videos.serializers import VideoSerializer


class TvSeriesDetailSerializer(serializers.ModelSerializer):
    """TvSeriesDetail model Serializer in tv details application"""

    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data Using TvSeriesDetailSerializer"""
        return VideoSerializer(obj.video).data

    class Meta:
        """Metadata for Tv series detail Serializer"""

        model = TvSeriesDetail
        fields = "__all__"


class TvSeasonSerializer(serializers.ModelSerializer):
    """TvSeason model Serializer in tv details application"""

    series = serializers.SerializerMethodField()

    def get_series(self, obj):
        """Method : get to Tv series data Using TvSeriesDetailSerializer"""
        return TvSeriesDetailSerializer(obj.series).data

    class Meta:
        """Metadata for Tv season Serializer"""

        model = TvSeason
        fields = "__all__"


class TvSeasonDetailSerializer(serializers.ModelSerializer):
    """TvSeasonDetail model Serializer in tv details application"""

    series = serializers.SerializerMethodField()

    def get_series(self, obj):
        """Method : get to TV series data Using TvSeriesDetailSerializer"""
        return TvSeriesDetailSerializer(obj.series).data

    class Meta:
        """Metadata for Tv season detail Serializer"""

        model = TvSeasonDetail
        fields = "__all__"
