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
    """
    Video API
    """,
    path("videos/", include("videos.urls")),
    path("discontinues/", include("video_providers.urls")),
    """
    User API
    """,
    path("users/", include("users.urls")),
    path("mypage/", include("mypages.urls")),
    path("mileages/", include("mileages.urls")),
    path("notifications/", include("notifications.urls")),
    """
    Group API
    """,
    path("applies/", include("applies.urls")),
    path("providers/", include("providers.urls")),
    path("groups/", include("groups.urls")),
    path("groups/<int:group_id>/account/", include("group_accounts.urls")),
    path("groups/<int:group_id>/reports/", include("reports.urls")),
    """
    Video history API
    """,
    path("mypage/recent-views/", include("recent_views.urls")),
    path("mypage/watch-marks/", include("watching_marks.urls")),
    path("mypage/wishes/", include("wishes.urls")),
    path("mypage/stars/", include("star_ratings.urls")),
    """
    API Documentation
    """,
    path("docs/schema/", SpectacularJSONAPIView.as_view(), name="docs"),  # api documentation file
    path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="docs"), name="swagger"),  # api docs by swagger
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="docs"), name="redoc"),  # api docs by redoc
]

# show debug toolbar only in DEBUG mode
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
