"""Configuration of users application"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Configuration details of users application"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
