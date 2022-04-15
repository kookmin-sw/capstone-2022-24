"""Configuration of notification application"""
from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    """Configuration details of notifications application"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "notifications"
