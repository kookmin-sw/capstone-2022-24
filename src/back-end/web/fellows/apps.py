"""Configuration of fellow application"""
from django.apps import AppConfig


class FellowsConfig(AppConfig):
    """Configuration details about fellow application"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "fellows"
