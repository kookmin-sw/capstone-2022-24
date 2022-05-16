"""wishes URL Configuration"""
from django.urls import path
from wishes.views import WishListView

urlpatterns = [
    path("", WishListView.as_view(), name="users_mypage_wishes"),
]
