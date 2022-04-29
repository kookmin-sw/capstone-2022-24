"""Wishes App Model Definitions: Wish"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from videos.models import Video


class Wish(models.Model):
    """Wish information that user wants to watch"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
    )
    date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        """Metadata for wish model"""

        db_table = "wish"

    def __str__(self):
        return f"찜 #{self.id}"
