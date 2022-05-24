"""URL Configuration of applies application"""
from applies.views import GroupApplyViewSet
from django.urls import path

urlpatterns = [
    path(
        "member/",
        GroupApplyViewSet.as_view({"put": "cancel_member", "post": "apply_member"}),
        name="member apply&cancel",
    ),
    path(
        "leader/",
        GroupApplyViewSet.as_view({"put": "cancel_leader", "post": "apply_leader"}),
        name="leader apply&cancel",
    ),
]
