"""URL configuration files"""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("videos/", include("videos.urls")),
    path("groups/", include("groups.urls")),
    path("users/", include("users.urls")),
    path("docs/schema/", SpectacularJSONAPIView.as_view(), name="docs"),  # api documentation file
    path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="docs"), name="swagger"),  # api docs by swagger
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="docs"), name="redoc"),  # api docs by redoc
    # auth
    path("users/", include("dj_rest_auth.urls")),
    path("users/", include("allauth.urls")),
]
