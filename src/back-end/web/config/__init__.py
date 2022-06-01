"""Initialize project settings"""
from __future__ import absolute_import

from config.tasks import app as celery

__all__ = ("celery",)
