"""wishes URL Configuration"""
from django.urls import path
from wishes.views import WishView

urlpatterns = [
    path("", WishView.as_view({"get": "list"}), name="users_mypage_wishes"),
]
