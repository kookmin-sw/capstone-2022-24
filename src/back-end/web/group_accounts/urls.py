"""group_accounts URL Configuration"""
from django.urls import path
from group_accounts.views import GroupAccountIDView, GroupAccountPWView

urlpatterns = [
    path("id/", GroupAccountIDView.as_view(), name="groups_account_id"),
    path("password/", GroupAccountPWView.as_view(), name="groups_account_pw"),
]
