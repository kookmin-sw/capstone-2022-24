"""Definitions of serializer for mileages application"""
from mileages.models import Mileage
from rest_framework import serializers
from users.serializers import UserSerializer


class MileageSerializer(serializers.ModelSerializer):
    """Mileage Serializer for json parsing"""

    class Meta:
        """Meta data for Mielage serializer"""

        model = Mileage
        fields = ["user", "amount", "renewal_date_time"]

    def get_user(self, obj):
        """Get user data using UserSerializer"""
        return UserSerializer(obj.user).data
