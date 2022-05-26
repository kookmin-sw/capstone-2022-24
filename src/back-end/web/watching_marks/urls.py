"""watching_marks URL Configuration"""
from django.urls import path
from watching_marks.views import WatchingMarkListView

urlpatterns = [
    path("", WatchingMarkListView.as_view(), name="users_mypage_wishes"),
]
