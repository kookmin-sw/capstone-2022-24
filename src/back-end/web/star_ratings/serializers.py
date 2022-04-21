"""Serializers of star_ratings application for json parsing"""
from rest_framework import serializers
from star_ratings.models import StarRating
from users.serializers import UserSerializer
from videos.serializers import VideoSerializer


class StarRatingSerializer(serializers.ModelSerializer):
    """Serializer of StarRating Model"""

    user = serializers.SerializerMethodField()
    video = serializers.SerializerMethodField()

    class Meta:
        """Metadata of StarRating serializer"""

        model = StarRating
        fields = "__all__"
        read_only_fields = "__all__"

    def get_user(self, obj):
        """Get user data using UserSerializer"""
        return UserSerializer(obj.user).data

    def get_video(self, obj):
        """Get video data using VideoSerializer"""
        return VideoSerializer(obj.video).data
