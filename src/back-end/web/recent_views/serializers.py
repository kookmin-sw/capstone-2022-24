"""Serializers of recent_views application for json parsing"""
from recent_views.models import RecentView
from rest_framework import serializers
from users.serializers import UserSerializer
from videos.serializers import VideoSerializer


class RecentViewSerializer(serializers.ModelSerializer):
    """Serializer of RecentView Model"""

    user = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()

    class Meta:
        """Metadata of RecentView serializer"""

        model = RecentView
        fields = "__all__"
        read_only_fields = "__all__"

    def get_user(self, obj):
        """Get user data using UserSerializer"""
        return UserSerializer(obj.user).data

    def get_video(self, obj):
        """Get video data using VideoSerializer"""
        return VideoSerializer(obj.video).data
