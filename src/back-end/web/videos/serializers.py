"""Serializers"""
from rest_framework import serializers
from videos.models import Video


class VideoSerializer(serializers.ModelSerializer):
    """Video information Serializing to get data"""

    class Meta:
        """Video Serializer field setting"""

        model = Video
        fields = ["tmdb_id", "title", "release_date", "film_rating", "category", "poster_key", "title_english"]
