"""Serializers of videos application for json parsing : VideoSerializer, VideoProviderSerialaizer"""
from rest_framework import serializers
from videos.models import Video, VideoDetail


class VideoSerializer(serializers.ModelSerializer):
    """Video model Serializer in videos application"""

    class Meta:
        """Metadata for videos Serializer"""

        model = Video
        fields = "__all__"


class VideoDetailSerializer(serializers.ModelSerializer):
    """VideoDetail model Serializer in videos application"""

    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data Using VideosDetailsSerialaizer"""
        return VideoSerializer(obj.video).data

    class Meta:
        """Metadata for videos details Serializer"""

        model = VideoDetail
        fields = "__all__"
