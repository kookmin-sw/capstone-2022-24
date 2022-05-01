"""Serializers of video_providers application for json parsing : VideoProviderSerialaizer"""
from rest_framework import serializers
from video_providers.models import VideoProvider


class VideoProviderSerialaizer(serializers.ModelSerializer):
    """Video Providers information Serializing to get data"""

    class Meta:
        """Video Providers Serializer field setting"""

        model = VideoProvider
        fields = ["videoId", "offerType", "link", "offerDate", "deadline"]
