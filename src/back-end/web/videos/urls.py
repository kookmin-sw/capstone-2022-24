"""videos URL Configuration"""
from django.urls import path
from videos.detail_views import DetailView
from videos.home_view import HomeView

urlpatterns = [
    path("", HomeView.as_view({"get": "list"}), name="home_video_list"),
    path("movie/<int:video_id>", DetailView.as_view({"get": "movie_details"}), name="movie_detail"),
]
