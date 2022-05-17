"""groups URL Configuration"""
from django.urls import path
from groups.views import GroupApplyView, GruopPaymentView

urlpatterns = [
    path("payments/", GruopPaymentView.as_view({"post": "payment"}), name="group payments"),
    path("applies/member/", GroupApplyView.as_view({"post": "apply_member"}), name="member apply"),
    path("applies/leader/", GroupApplyView.as_view({"post": "apply_leader"}), name="leader apply"),
    path("applies/member/", GroupApplyView.as_view({"put": "cancel_member"}), name="member refund"),
    path("applies/leader/", GroupApplyView.as_view({"put": "cancel_leader"}), name="leader cancel"),
]
