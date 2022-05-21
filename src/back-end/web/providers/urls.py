"""providers URL Configuration"""
from django.urls import path
from groups.views import GroupDetailView
from providers.views import ProviderListByApplyTypeView

urlpatterns = [
    path("", ProviderListByApplyTypeView.as_view(), name="users_providers"),
    path("<int:provider_id>/", GroupDetailView.as_view(), name="groups_detail_by_provider"),  # TODO: refactoring needed
]
