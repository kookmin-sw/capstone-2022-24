"""Celery worker & scheduler settings"""
from celery import Celery
from django.conf import settings

# is it needed?
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("config", broker=settings.CELERY_BROKER_URL)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Celery beat settings
app.conf.beat_schedule = {
    # periodic events like this
    # "periodic_add_numbers": {
    #     "task": "my_app.tasks.add_numbers",
    #     "schedule": crontab(minute="*\1"),
    # },
}


@app.task(bind=True)
def debug_task(self):
    """(sample) Debug tasks"""
    print(f"Request: {self.request!r}")
