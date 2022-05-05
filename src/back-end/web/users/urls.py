"""Users URL Configuration"""
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.views import LoginView, LogoutView
from django.urls import path

from users.views import (
    SignUpView,
    NaverLoginView,
    GoogleLoginView,
    ValidateNicknameView,
    ValidateProfileImageView,
    ValidateWithdrawalView,
    ProfileImageCreateView,
    UserWithdrawalView,
)

urlpatterns = [
    # Supported apis
    # - GET /users/user/
    # - PUT /users/user/
    # - PATCH /users/user/
    # - POST /users/verify-email/
    # - POST /users/login/
    # - POST /users/logout/
    # - POST /users/password/change/
    # - POST /users/password/reset/
    # - POST /users/password/reset/confirm/
    # - POST /uesrs/token/refresh/
    # - POST /users/token/verify/
    # path("", include("dj_rest_auth.urls")),

    # oauth2 login
    path("login/oauth/naver/", NaverLoginView.as_view(), name="users_login_oauth_naver"),
    path("login/oauth/google/", GoogleLoginView.as_view(), name="users_login_oauth_google"),

    # Supported api
    # - POST /users/
    # - POST /users/resend-email/
    # - POST /users/verify-email/
    # path("", include("dj_rest_auth.registration.urls")),

    # sign up
    path("", SignUpView.as_view(), name="users_signup"),

    # token refresh
    path("token/", get_refresh_view().as_view(), name="token_refresh"),

    # normal login / logout
    path("login/", LoginView.as_view(), name="login"),  # 일반 로그인 (미사용)
    path("logout/", LogoutView.as_view(), name="logout"),  # 로그아웃 (미사용)

    # validate user fields
    path("validate-nickname/", ValidateNicknameView.as_view(), name="users_validate_nickname"),
    path("validate-profile-image/", ValidateProfileImageView.as_view(), name="users_alidate_profile_image"),
    path("profile-image/", ProfileImageCreateView.as_view(), name="users_upload_profile_image"),

    # withdrawal
    path("<str:nickname>/validate-withdrawal/", ValidateWithdrawalView.as_view(), name="users_nickname_validate_withdrawal"),
    path("", UserWithdrawalView.as_view(), name="users_withdrawal")
]

# /token
# /login
# /logout
# /users/validate-nickname
# /users/validate-profile-images
# /users/profile-images
# /users/{nickname}/validate-withdrawal
# /users
