"""URL configuration files"""
from django.urls import path
from mypages.views import MyPageDetailView

urlpatterns = [
    path("", MyPageDetailView.as_view(), name="users_mypage_detail"),
]
