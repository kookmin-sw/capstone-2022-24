"""Serializers of wish application for json parsing"""
from rest_framework import serializers
from users.serializers import UserSerializer
from videos.serializers import VideoSerializer
from wishes.models import Wish


class WishSerializer(serializers.ModelSerializer):
    """Serializer of Wish model"""

    user = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()

    class Meta:
        """Metadata of Wish serializer"""

        model = Wish
        fields = "__all__"
        read_only_fields = "__all__"

    def get_user(self, obj):
        """Get user data using UserSerializer"""
        return UserSerializer(obj.user).data

    def get_video(self, obj):
        """Get video data using UserSerializer"""
        return VideoSerializer(obj.video).data
