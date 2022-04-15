"""Application settings of mileages application"""
from django.apps import AppConfig


class MileagesConfig(AppConfig):
    """Configurations about mileages application"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "mileages"
