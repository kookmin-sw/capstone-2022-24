"""wishes URL Configuration"""
from django.urls import path
from wishes.views import WishViewSet

urlpatterns = [
    path("", WishViewSet.as_view({"get": "list"}), name="users_mypage_wishes"),
]
