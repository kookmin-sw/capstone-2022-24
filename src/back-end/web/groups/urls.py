"""groups URL Configuration"""
from django.urls import path
from groups.views import GruopPaymentView

urlpatterns = [
    path("payments/", GruopPaymentView.as_view({"post": "payment"}), name="group payments"),
]
