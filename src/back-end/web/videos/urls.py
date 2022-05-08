"""videos URL Configuration"""
from django.urls import path
from videos.views import HomeView

urlpatterns = [
    path("", HomeView.as_view({"get": "list"})),
]
