"""videos URL Configuration"""
from django.urls import path
from videos.home_view import HomeView

urlpatterns = [
    path("", HomeView.as_view({"get": "list"}), name="home_video_list"),
]
