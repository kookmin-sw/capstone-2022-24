"""Celery worker & scheduler settings"""
from __future__ import absolute_import, unicode_literals

from celery import Celery
from django.conf import settings

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Celery beat settings
app.conf.timezone = "Asia/Seoul"
app.conf.beat_schedule = {
    # periodic events like this
    # "periodic_add_numbers": {
    #     "task": "config.tasks.add_numbers",
    #     "schedule": crontab(),
    #     "args": (1, 1),
    # },
}
