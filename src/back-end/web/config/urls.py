"""URL configuration files"""
from django.conf import settings
from django.conf.urls.static import static
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
    path("groups/<int:group_id>/account/", include("group_accounts.urls")),
    path("users/", include("users.urls")),
    path("groups/applies/", include("applies.urls")),
    path("users/mypage/", include("mypages.urls")),
    path("discontinues/", include("video_providers.urls")),
    # api docs
    path("docs/schema/", SpectacularJSONAPIView.as_view(), name="docs"),  # api documentation file
    path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="docs"), name="swagger"),  # api docs by swagger
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="docs"), name="redoc"),  # api docs by redoc
    # video history
    path("users/mypage/recent-views/", include("recent_views.urls")),
    path("users/mypage/watch-marks/", include("watching_marks.urls")),
    path("users/mypage/wishes/", include("wishes.urls")),
    path("users/mypage/stars/", include("star_ratings.urls")),
]

# show debug toolbar only in DEBUG mode
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
