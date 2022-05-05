"""Serializers of video_providers application for json parsing : VideoProviderSerialaizer"""
from providers.serializers import ProviderSerializer
from rest_framework import serializers
from video_providers.models import VideoProvider
from videos.serializers import VideoSerializer


class VideoProviderSerializers(serializers.ModelSerializer):
    """Video Providers information Serializing to get data"""

    video = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data Using VideoProviderSerializers"""
        return VideoSerializer(obj.video).data

    def get_provider(self, obj):
        """Method : get to provider data using VideoProviderSerializers"""
        return ProviderSerializer(obj.provider).data

    class Meta:
        """Video Providers Serializer field setting"""

        model = VideoProvider
        fields = "__all__"
