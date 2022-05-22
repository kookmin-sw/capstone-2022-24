"""video provider URL Configuration"""
from django.urls import path
from video_providers.views import DiscontinuityClass

urlpatterns = [
    path("7/", DiscontinuityClass.as_view({"get": "get_discontinue_videos_after_7_days"}), name="7days"),
    path("15/", DiscontinuityClass.as_view({"get": "get_discontinue_videos_after_15_days"}), name="15days"),
    path("30/", DiscontinuityClass.as_view({"get": "get_discontinue_videos_after_30_days"}), name="30days"),
]
