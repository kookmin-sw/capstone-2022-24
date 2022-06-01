"""notifications URL Configuration"""
from django.urls import path
from notifications.views import NotificationListAndUpdateView

urlpatterns = [path("", NotificationListAndUpdateView.as_view(), name="notifications")]
