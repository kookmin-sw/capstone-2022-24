"""APIs of users application"""
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import RegisterView, SocialLoginView
from django.conf import settings
from rest_framework.generics import CreateAPIView, GenericAPIView


class NaverLoginView(SocialLoginView):
    """Login with Naver account"""

    adapter_class = NaverOAuth2Adapter
    client_class = OAuth2Client


class GoogleLoginView(SocialLoginView):
    """Login with Google account"""

    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = f"{settings.APP_HOST}:{settings.APP_PORT}/login/naver"


class SignUpView(RegisterView):
    """Sign up with nickname(required) and profile image(optional)"""

    # TODO


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
