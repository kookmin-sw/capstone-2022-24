"""Videos App Model Serializer: Video, VideoDetail"""
from rest_framework import serializers

from .models import Video, VideoDetail


class VideosSerialaizer(serializers.ModelSerializer):
    """Video information Serializing to data create, update"""

    class Meta:
        """Video Serializer field setting"""

        model = Video
        fields = ["tmdb_id", "title", "release_date", "film_rating", "category", "poster_key", "title_english"]


class VideosDetailsSerialaizer(serializers.ModelSerializer):
    """Video detail information Serializing to data create, update"""

    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data"""
        return VideosSerialaizer(obj.video).data

    class Meta:
        """Video Serializer field setting"""

        model = VideoDetail
        fields = [
            "runtime",
            "ratings",
            "production_countries",
            "gernes",
        ]
