"""videos URL Configuration"""
from django.urls import path
from videos.detail_views import DetailView, tv_season_redirect_view
from videos.home_view import HomeView

urlpatterns = [
    path("", HomeView.as_view({"get": "list"}), name="home_video_list"),
    path("tv/<int:video_id>", tv_season_redirect_view, name="redirect_tv_detail"),
    path("tv/<int:video_id>/seasons/<int:season_num>", DetailView.as_view({"get": "tv_details"}), name="tv_details"),
]
