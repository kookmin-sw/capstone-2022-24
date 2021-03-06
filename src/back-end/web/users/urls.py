"""Users URL Configuration"""
from django.urls import path
from users.views import (
    GeneralLoginView,
    GeneralLogoutView,
    GoogleLoginView,
    NaverLoginView,
    ProfileImageUploadView,
    RefreshTokenView,
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
    path("token/", RefreshTokenView.as_view(), name="users_token_refresh"),
    # normal login / logout (perhaps used someday)
    path("login/", GeneralLoginView.as_view(), name="login"),
    path("logout/", GeneralLogoutView.as_view(), name="logout"),
    # validate user fields
    path("validate-nickname/", ValidateNicknameView.as_view(), name="users_validate_nickname"),
    path("validate-profile-image/", ValidateProfileImageView.as_view(), name="users_validate_profile_image"),
    path("profile-images/", ProfileImageUploadView.as_view(), name="users_upload_profile_image"),
    # withdrawal
    path(
        "<str:nickname>/validate-withdrawal/",
        ValidateWithdrawalView.as_view(),
        name="users_nickname_validate_withdrawal",
    ),
    path("", UserWithdrawalView.as_view(), name="users_withdrawal"),
]
