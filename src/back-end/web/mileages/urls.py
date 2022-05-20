"""mileages URL Configuration"""
from django.urls import path
from mileages.views import MileageViewSet

urlpatterns = [path("mileages/", MileageViewSet.as_view, "mileages")]
