"""Definitions of watching mark models: WatchingMark"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from videos.models import Video


class WatchingMark(models.Model):
    """Definition of whether to watch check model"""

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
        """Metadata for watching_mark model"""

        db_table = "watching_mark"

    def __str__(self):
        return f"작품 관람 #{self.id}"
