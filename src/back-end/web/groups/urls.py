"""groups URL Configuration"""
from django.urls import path
from groups.views import GroupDetailView, GruopPaymentView

urlpatterns = [
    path("payments/", GruopPaymentView.as_view({"post": "payment"}), name="group payments"),
    path("<int:group_id>/", GroupDetailView.as_view(), name="groups_detail"),
]
