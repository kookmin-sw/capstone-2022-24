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

    def get_user(self, user):
        """Get user details of mypage owner"""
        return UserSerializer(user).data

    def get_groups(self, obj):
        """Get groups details of mypage owner"""
        return MyPageGroupSerializer(obj)

    def get_videos(self, obj):
        """Get videos list that user checked"""
