"""Settings about celery module"""
from celery import Celery

# config 프로젝트를 사용하도록 설정
app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """Get history"""
    print(f"Request: {self.request:0!r}")
