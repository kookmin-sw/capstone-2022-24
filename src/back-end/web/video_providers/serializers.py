"""Serializers of video_providers application for json parsing : VideoProviderSerialaizer"""
from providers.serializers import ProviderListSerializer, ProviderSerializer
from rest_framework import serializers
from video_providers.models import VideoProvider
from videos.serializers import VideoSerializer, VideoListSerializer


class VideoProviderSerializer(serializers.ModelSerializer):
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

class ProviderLinkSerializer(serializers.ModelSerializer):
    provider= serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    
    def get_provider(self, obj):
        """Method : get to provider data using DiscontinuityVideoSerializer"""
        return ProviderListSerializer(obj.provider).data
    
    def get_link(self, obj):
        """Method : 링크 주는 거"""
        return obj.link 

    class Meta:
        """Video Providers Serializer field setting"""

        model = VideoProvider
        fields = ["video","provider","link"]



class DiscontinuityVideoSerializer(serializers.ModelSerializer):
    """Discontinuity Video Providers information Serializing to get data"""

    video = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()

    def get_video(self, obj):
        """Method : get to Video data Using DiscontinuityVideoSerializer"""
        return VideoListSerializer(obj.video).data

    def get_provider(self, obj):
        """Method : get to provider data using DiscontinuityVideoSerializer"""
        return ProviderLinkSerializer(obj).data

    class Meta:
        """Video Providers Serializer field setting"""

        model = VideoProvider
        fields = ["video","provider","link"]
