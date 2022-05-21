"""mileages URL Configuration"""
from django.urls import path
from mileages.views import MileageViewSet

urlpatterns = [
    path("", MileageViewSet.as_view({"get": "list", "post": "create", "patch": "partial_update"}), name="mileages")
]
