"""Serializers of users application"""
from accounts.serializers import AccountSerializer
from dj_rest_auth.registration.serializers import (
    RegisterSerializer,
    SocialLoginSerializer,
)
from dj_rest_auth.serializers import LoginSerializer
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
            "name",
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


class UserLoginSerializer(LoginSerializer):
    """Authenticate user with nickname and password fields"""

    username = None
    email = serializers.EmailField(required=True, allow_blank=False)
    nickname = serializers.CharField(required=True, allow_blank=False)

    def update(self, instance, validated_data):
        """Update user"""
        return

    def create(self, validated_data):
        """Create user"""
        return


class UserSignUpSerializer(RegisterSerializer):
    """Needed information when user signs up"""

    # TODO

    def update(self, instance, validated_data):
        """(Not used) Inherit abstract method"""

    def create(self, validated_data):
        """(Not used) Inherit abstract method"""


class NaverLoginSerializer(SocialLoginSerializer):
    """Needed information when user login with Naver"""

    access_token = None
    id_token = None

    def update(self, instance, validated_data):
        """(Not used) Inherit abstract method"""

    def create(self, validated_data):
        """(Not used) Inherit abstract method"""


class GoogleLoginSerializer(SocialLoginSerializer):
    """Needed information when user login with Google"""

    id_token = None
    code = None

    def update(self, instance, validated_data):
        """(Not used) Inherit abstract method"""

    def create(self, validated_data):
        """(Not used) Inherit abstract method"""
