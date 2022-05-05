"""Serializers of video_total_counts application for json parsing : VideoTotalCountSerialaizer"""
from rest_framework import serializers
from video_total_counts.models import VideoTotalCount


class VideoTotalCountSerializer(serializers.ModelSerializer):
    """Video total Count model Serializer in video_total_counts application"""

    class Meta:
        """Metadata for video total count Serializer"""

        model = VideoTotalCount
        fields = "__all__"
