"""Serializers of notification models for json parsing"""
from notifications.models import Notification, NotificationContent
from providers.serializers import ProviderSerializer
from rest_framework import serializers
from users.serializers import UserSerializer


class NotificationContentSerializer(serializers.ModelSerializer):
    """Serializer of notification content model"""

    class Meta:
        """Metadata of notification content serializer"""

        model = NotificationContent
        fields = "__all__"
        read_only_fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    """Serializer of notification model"""

    user = serializers.SerializerMethodField()
    provider = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    class Meta:
        """Metadata of notification serializer"""

        model = Notification
        fields = "__all__"
        read_only_fields = ("user", "provider", "content", "creation_date_time")

    def get_user(self, obj):
        """Get user data using UserSerializer"""
        return UserSerializer(obj.user).data

    def get_provider(self, obj):
        """Get provider data using ProviderSerializer"""
        return ProviderSerializer(obj.provider).data

    def get_content(self, obj):
        """Get notification details using NotificationContentSerializer"""
        return NotificationContentSerializer(obj.content).data
