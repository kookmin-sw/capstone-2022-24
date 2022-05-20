"""video provider URL Configuration"""
from django.urls import path
from video_providers.views import DiscontinuityClass

urlpatterns = [
    path("7/", DiscontinuityClass.as_view({"get": "day_7"}), name="7days"),
    path("15/", DiscontinuityClass.as_view({"get": "day_15"}), name="15days"),
    path("30/", DiscontinuityClass.as_view({"get": "day_30"}), name="30days"),
]
