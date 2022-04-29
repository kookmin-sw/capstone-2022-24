"""Definitions of serializer for mileages application"""
from mileages.models import Mileage
from rest_framework import serializers
from users.serializers import UserSerializer


class MileageSerializer(serializers.ModelSerializer):
    """Mileage Serializer for json parsing"""

    user = serializers.SerializerMethodField()

    class Meta:
        """Meta data for Mielage serializer"""

        model = Mileage
        fields = "__all__"

    def get_user(self, obj):
        """Get user data using UserSerializer"""
        return UserSerializer(obj.user).data
