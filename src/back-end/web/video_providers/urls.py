from django.urls import path
from video_providers.views import DiscontinuityClass

urlpatterns = [
    path("7days/", DiscontinuityClass.as_view({"get": "day_7"}), name="7days"),  # /discontinues/7days
    path("15days/", DiscontinuityClass.as_view({"get": "day_15"}), name="15days"),  # /discontinues/15days
    path("30days/", DiscontinuityClass.as_view({"get": "day_30"}), name="30days"),  # /discontinues/30days
]
