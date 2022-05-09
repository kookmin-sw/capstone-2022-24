"""Users URL Configuration"""
from dj_rest_auth.jwt_auth import get_refresh_view
from django.urls import path
from users.views import (
    GeneralLoginView,
    GeneralLogoutView,
    GoogleLoginView,
    NaverLoginView,
    ProfileImageCreateView,
    SignUpView,
    UserWithdrawalView,
    ValidateNicknameView,
    ValidateProfileImageView,
    ValidateWithdrawalView,
)

urlpatterns = [
    # oauth2 login
    path("login/oauth/naver/", NaverLoginView.as_view(), name="users_login_oauth_naver"),
    path("login/oauth/google/", GoogleLoginView.as_view(), name="users_login_oauth_google"),
    # sign up
    path("", SignUpView.as_view(), name="users_signup"),
    # token refresh
    path("token/", get_refresh_view().as_view(), name="token_refresh"),
    # normal login / logout (perhaps used someday)
    path("login/", GeneralLoginView.as_view(), name="login"),
    path("logout/", GeneralLogoutView.as_view(), name="logout"),
    # validate user fields
    path("validate-nickname/", ValidateNicknameView.as_view(), name="users_validate_nickname"),
    path("validate-profile-image/", ValidateProfileImageView.as_view(), name="users_alidate_profile_image"),
    path("profile-image/", ProfileImageCreateView.as_view(), name="users_upload_profile_image"),
    # withdrawal
    path(
        "<str:nickname>/validate-withdrawal/",
        ValidateWithdrawalView.as_view(),
        name="users_nickname_validate_withdrawal",
    ),
    path("", UserWithdrawalView.as_view(), name="users_withdrawal"),
]
