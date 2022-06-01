"""Celery worker & scheduler settings"""
from __future__ import absolute_import, unicode_literals

from celery import Celery, shared_task
from django.conf import settings

# is it needed?
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Celery beat settings
app.conf.timezone = "Asia/Seoul"
app.conf.beat_schedule = {
    # periodic events like this
    "periodic_add_numbers": {
        "task": "config.tasks.add_numbers",
        # "schedule": crontab(),
        "schedule": 5.0,
        "args": (1, 1),
    },
}


@shared_task
def add_numbers(a, b):
    """(sample) add numbers"""
    print("add_numbers are called:", a + b)
    print("hi!!!")
    return a + b


@shared_task
def sub_numbers(a, b):
    """(sample) subtract numbers"""
    print("sub numbers: a-b", a - b)
    return a - b


@app.task(bind=True)
def debug_task(self):
    """(sample) Debug tasks"""
    print(f"Request: {self.request!r}")
