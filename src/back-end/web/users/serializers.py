"""Serializers of users application"""
from accounts.serializers import AccountSerializer
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """User model serializer in users application"""

    account = serializers.SerializerMethodField()

    class Meta:
        """Metadata of UserSerializer"""

        model = User
        fields = "__all__"
        read_only_fields = [
            "nickname",
            "email",
            "cellPhoneNumber",
            "birthday",
            "isBlocked",
            "registrationDateTime",
            "withdrawalDateTime",
        ]

    def get_account(self, obj):
        """Get account data using AccountSerializer"""
        return AccountSerializer(obj.account).data
