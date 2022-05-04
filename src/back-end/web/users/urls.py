"""Users URL Configuration"""
from django.urls import include, path

# router = DefaultRouter()
# router.register(r"", views.UserViewSet)
from users.views import NaverLogin, GoogleLogin

urlpatterns = [
    # path("", include(router.urls)),
    path("", include("dj_rest_auth.urls")),
    path("", include("dj_rest_auth.registration.urls")),
    path("", include("allauth.urls")),
    path("login/oauth/naver/", NaverLogin.as_view(), name="naver_login"),
    path("login/oauth/google/", GoogleLogin.as_view(), name="google_login")
    # path("login/oauth/", views.google_login, name="google_login"),
    # path("google/callback/", views.google_callback, name="google_callback"),
    # path("google/login/finish/", views.GoogleLogin.as_view(), name="google_login_todjango"),
    # path("login/oauth/google/", views.GoogleLogin.as_view(), name="google_login"),
    # path("login/oauth/naver/", views.NaverLogin.as_view(), name="naver_login"),
    # path("google/login/{", views.google_login, name="google_login"),
    # path("google/callback/", views.google_callback,      name="google_callback"),
    # path("google/login/finish/", views.GoogleLogin.as_view(), name="google_login_todjango"),
]

# /login/oauth/{social_type}
# /users
# /token
# /login
# /logout
# /users/validate-nickname
# /users/validate-profile-images
# /users/profile-images
# /users/{nickname}/validate-withdrawal
# /users/{nickname}
# /users/mypage
# /users/mypage/recent-views
# /users/mypage/watch-marks
# /users/mypage/dibs
# /users/mypage/stars
# /users/notifications
# /users/notifications
# /users/notifications/{notification_id}
