"""Serializers of movie detail application for json parsing : MovieDetailSerializer"""
from movie_details.models import MovieDetail
from rest_framework import serializers
from videos.serializers import VideoSerializer


class MovieDetailSerializer(serializers.ModelSerializer):
    """MovieDetail model Serializer in movie details application"""

    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data Using MovieDetailSerializer"""
        return VideoSerializer(obj.video).data

    class Meta:
        """Metadata for videos Serializer"""

        model = MovieDetail
        fields = "__all__"
