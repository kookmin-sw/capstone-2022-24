"""URL Configuration of applies application"""
from applies.views import GroupApplyView
from django.urls import path

urlpatterns = [
    path("member/", GroupApplyView.as_view({"put": "cancel_member", "post": "apply_member"}), name="member by group"),
    path("leader/", GroupApplyView.as_view({"put": "cancel_leader", "post": "apply_leader"}), name="leader apply"),
]

"""
    path("member/", GroupApplyView.as_view(), name="member apply"),
    path("leader/", GroupApplyView.as_view(), name="leader apply"),
    path("member/", GroupApplyView.as_view(), name="member refund"),
    path("leader/", GroupApplyView.as_view(), name="leader cancel"),
"""
