"""Mypage serializers for json parsing"""
from groups.serializers import MyPageGroupSerializer
from rest_framework import serializers
from users.serializers import UserSerializer


class MyPageSerializer(serializers.Serializer):
    """Mypage serializer including user, wishes, recent-views, star-ratings, watching-marks information"""

    profile = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()
    videos = serializers.SerializerMethodField()

    def update(self, instance, validated_data):
        """Do nothing because mypage is read-only"""

    def create(self, validated_data):
        """Do nothing because mypage is read-only"""

    def get_profile(self, user):
        """Get user details of mypage owner"""
        return UserSerializer(user).data

    def get_groups(self, user):
        """Get groups details of mypage owner"""
        return MyPageGroupSerializer(user)

    def get_videos(self, user):
        """Get videos list that user checked"""
