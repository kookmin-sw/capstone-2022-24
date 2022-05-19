"""videos URL Configuration"""
from django.urls import path
from videos.views.detail_views import DetailView, tv_season_redirect_view
from videos.views.home_views import HomeView
from wishes.views import WishCreateAndDestroyView

urlpatterns = [
    path("", HomeView.as_view({"get": "list"}), name="home_video_list"),
    path("tv/<int:video_id>/", tv_season_redirect_view, name="redirect_tv_detail"),
    path("tv/<int:video_id>/seasons/<int:season_num>/", DetailView.as_view({"get": "tv_details"}), name="tv_details"),
    path("movie/<int:video_id>/", DetailView.as_view({"get": "movie_details"}), name="movie_detail"),
    # wish
    path("<int:video_id>/wishes/", WishCreateAndDestroyView.as_view(), name="video_wish"),
]
