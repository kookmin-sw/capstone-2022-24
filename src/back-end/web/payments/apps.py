"""Configurations of payments application"""
from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    """Configuration details of payments application"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "payments"
