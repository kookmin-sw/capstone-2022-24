"""APIs of users application"""
from allauth.account import app_settings
from allauth.account.utils import complete_signup
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.utils import get_username_max_length
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.serializers import JWTSerializer
from django.conf import settings
from django.contrib.auth import get_user_model
from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
    inline_serializer,
)
from rest_framework import serializers, status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from users.serializers import (
    GoogleLoginSerializer,
    NaverLoginSerializer,
    UserSignUpVerifySerializer,
)

UserModel = get_user_model()


@extend_schema(
    operation_id="Naver Login",
    parameters=[
        OpenApiParameter(
            name="set-cookie ",
            description="ongot-token={{Access Token}}; expires=DAY, DD MON 2022 hh:mm:ss GMT; Max-Age=39600;",
            type=str,
            location=OpenApiParameter.COOKIE,
            response=True,
        ),
        OpenApiParameter(
            name="set-cookie",
            description="ongot-refresh-token={{Refresh Token}}; expires=DAY, DD MON 2022 hh:mm:ss GMT; Max-Age=54000;",
            type=str,
            location=OpenApiParameter.COOKIE,
            response=True,
        ),
    ],
    responses={
        200: OpenApiResponse(
            description="네이버 로그인 성공",
            response=JWTSerializer,
        )
    },
)
class NaverLoginView(SocialLoginView):
    """Login with Naver account"""

    adapter_class = NaverOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = NaverLoginSerializer
    callback_url = f"{settings.APP_HOST}:{settings.APP_PORT}"


@extend_schema(
    operation_id="Google Login",
    parameters=[
        OpenApiParameter(
            name="set-cookie ",
            description="ongot-token={{ Access Token }}",
            type=str,
            location="cookie",
            response=True,
        ),
        OpenApiParameter(
            name="set-cookie",
            description="ongot-refresh-token={{ Refresh Token }}",
            type=str,
            location="cookie",
            response=True,
        ),
    ],
    responses={
        200: OpenApiResponse(
            description="구글 로그인 성공",
            response=JWTSerializer,
        )
    },
)
class GoogleLoginView(SocialLoginView):
    """Login with Google account"""

    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = GoogleLoginSerializer
    callback_url = f"{settings.APP_HOST}:{settings.APP_PORT}"


@extend_schema(
    operation_id="회원 가입",
    responses={
        200: OpenApiResponse(
            description="회원 가입 성공",
            response=inline_serializer(
                name="VerifyUserSerializer",
                fields={
                    "nickname": serializers.CharField(
                        max_length=get_username_max_length(),
                        min_length=app_settings.USERNAME_MIN_LENGTH,
                        required=app_settings.USERNAME_REQUIRED,
                        validators=[UniqueValidator(queryset=UserModel.objects.all())],
                    ),
                    "profile_image_url": serializers.URLField(required=False),
                    "name": serializers.CharField(),
                    "email": serializers.EmailField(),
                    "is_verified": serializers.BooleanField(),
                },
            ),
        )
    },
)
class SignUpView(CreateAPIView):
    """Sign up with nickname(required) and profile image(optional)"""

    serializer_class = UserSignUpVerifySerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        """Save user's nickname & profile"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        data = self.get_response_data(user)
        return Response(data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        complete_signup(self.request, user, settings.ACCOUNT_EMAIL_VERIFICATION, settings.ACCOUNT_SIGNUP_REDIRECT_URL)
        return user

    def get_response_data(self, user):
        """Get serializer + other user context data"""
        return {
            "name": user.name,
            "nickname": user.nickname,
            "profile_image_url": user.profile_image_url,
            "email": user.email,
            "is_verified": user.is_verified,
        }


class ValidateNicknameView(GenericAPIView):
    """Validation about nickname when user sign up"""

    # TODO


class ValidateProfileImageView(GenericAPIView):
    """Validation about profile image to use"""

    # TODO


class ProfileImageCreateView(CreateAPIView):
    """Upload profile image of user"""

    # TODO


class ValidateWithdrawalView(GenericAPIView):
    """Validation about user's withdrawal using whether to join groups"""

    # TODO


class UserWithdrawalView(GenericAPIView):
    """Withdrawal by checking whether to delete"""

    # TODO
