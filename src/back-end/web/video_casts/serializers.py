"""Serializers of video catsts application for json parsing : VideoCastSerializer"""
from rest_framework import serializers
from video_casts.models import VideoCast
from videos.serializers import VideoSerializer


class VideoCastSerializer(serializers.ModelSerializer):
    """VideoCast model Serializer in video casts application"""

    video = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data Using VideoCastSerializer"""
        return VideoSerializer(obj.video).data

    class Meta:
        """Metadata for videos Serializer"""

        model = VideoCast
        fields = "__all__"
