"""videos URL Configuration"""
from django.urls import path
from videos.detail_views import DetailView
from videos.home_view import HomeView

urlpatterns = [
    path("", HomeView.as_view({"get": "list"}), name="home_video_list"),
    path("tv/<int:video_id>/<int:season_id>", DetailView.as_view({"get": "tv_details"}), name="tv_details"),
]
