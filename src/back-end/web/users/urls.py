"""Users URL Configuration"""
from django.urls import include, path

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("", include("dj_rest_auth.registration.urls")),
    path("", include("allauth.urls")),
]
