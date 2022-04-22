"""Initialization file of ongot config project"""
from .celery import app as celery_app

__all__ = ("celery_app",)
