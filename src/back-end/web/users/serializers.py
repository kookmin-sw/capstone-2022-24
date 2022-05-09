"""Serializers of users application"""
# pylint: disable=W0221
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from users.adapter import UserAccountAdapter
from users.models import User
from users.validators import get_nickname_validators, get_unique_nickname_validator


class UserSerializer(serializers.ModelSerializer):
    """User Detail serializer after login"""

    class Meta:
        """Metadata of UserSerializer"""

        model = User
        fields = [
            "nickname",
            "name",
            "email",
            "cell_phone_number",
            "profile_image_url",
            "birthday",
            "is_active",
            "is_verified",
        ]


class UserLoginSerializer(LoginSerializer):
    """Authenticate user with nickname/email/password fields before login"""

    username = None
    email = serializers.EmailField(required=True, allow_blank=False)
    nickname = serializers.CharField(required=True, allow_blank=False)

    def update(self, instance, validated_data):
        """Update user"""
        return

    def create(self, validated_data):
        """Create user"""
        return


class UserSignUpVerifySerializer(serializers.ModelSerializer):
    """Needed information when user signs up"""

    cleaned_data = None

    class Meta:
        """Metadata for UserSignUpVerifySerializer"""

        model = User
        fields = ["nickname", "profile_image_url"]
        extra_kwargs = {
            "nickname": {
                "required": True,
                "validators": get_nickname_validators() + [get_unique_nickname_validator(User.objects.all())],
            },
            "profile_image_url": {"required": False},
        }

    def get_cleaned_data(self):
        """Get validated form data"""
        return {
            "nickname": self.validated_data.get("nickname", ""),
            "profile_image_url": self.validated_data.get("profile_image_url", ""),
        }

    def save(self, request):
        """Save user nickname & profile image and verify user"""
        adapter = UserAccountAdapter()
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, request.user, self, commit=False)
        # validate nickname
        if "nickname" in self.cleaned_data:
            try:
                adapter.clean_username(self.cleaned_data["nickname"])
            except DjangoValidationError as exc:
                raise serializers.ValidationError(detail=serializers.as_serializer_error(exc))
        # verify user account after validation
        user.is_verified = True
        # save all changes
        user.save()
        return user


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


class NicknameSerializer(serializers.ModelSerializer):
    """Validate nickname serializer"""

    class Meta:
        """Metadata of UserSerializer"""

        model = User
        fields = ["nickname"]
        extra_kwargs = {
            "nickname": {
                "required": True,
                "validators": get_nickname_validators() + [get_unique_nickname_validator(User.objects.all())],
            },
        }
