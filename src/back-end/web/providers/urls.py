"""providers URL Configuration"""
from django.urls import path
from providers.views import ProviderListByApplyTypeView

urlpatterns = [
    path("", ProviderListByApplyTypeView.as_view(), name="users_providers"),
]
