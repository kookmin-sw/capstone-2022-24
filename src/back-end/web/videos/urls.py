"""videos URL Configuration"""
from django.urls import path, re_path
from videos.views import HomeView

urlpatterns = [
    re_path(r"^(?P<search>P<categories>P<providers>P<page>P<size>)$", HomeView.as_view({"get": "list"})),
    path("", HomeView.as_view({"get": "list"})),
]
