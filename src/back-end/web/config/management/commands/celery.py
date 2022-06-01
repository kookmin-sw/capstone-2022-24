"""Autoreload celery process"""
import os
import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload


def restart_celery():
    """Restart celery"""
    cmd = "pkill -f celery"
    subprocess.call(shlex.split(cmd))

    env = os.environ.copy()  # current environment variables
    env.update({"C_FORCE_ROOT": "1"})  # update environment variables

    cmd = "celery worker -A config --loglevel=info"
    subprocess.call(shlex.split(cmd), env=env)


class Command(BaseCommand):
    """Commands to handle django project"""

    def handle(self, *args, **options):
        """Celery reload when django code changes"""
        print("Starting celery worker with autoreload...")
        autoreload.run_with_reloader(restart_celery)
