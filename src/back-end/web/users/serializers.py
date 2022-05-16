"""Serializers of users application"""
from accounts.serializers import AccountSerializer
from rest_framework import serializers
from users.models import SocialType, User


class SocialTypeSerializer(serializers.ModelSerializer):
    """SocialType model serializer in users application"""

    class Meta:
        """Metadata of SocialTypeSerializer"""

        model = SocialType
        fields = "__all__"
        extra_kwargs = {"name": {"read_only": True}, "logoKey": {"read_only": True}}


class UserSerializer(serializers.ModelSerializer):
    """User model serializer in users application"""

    social_type = serializers.SerializerMethodField()
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

    def get_social_type(self, obj):
        """Get social type data using SocialTypeSerializer"""
        return SocialTypeSerializer(obj.social_type).data

    def get_account(self, obj):
        """Get account data using AccountSerializer"""
        return AccountSerializer(obj.account).data
