"""Definitions of watching mark models: WatchingMark"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from videos.models import Video


class WatchingMark(models.Model):
    """Definition of whether to watch check model"""

    id = models.BigAutoField(
        primary_key=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
    )
    video = models.ForeignKey(
        Video,
        null=False,
        on_delete=models.CASCADE,
    )
    date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        """Metadata for watching_mark model"""

        db_table = "watching_mark"

    def __str__(self):
        return f"{self.user}님이 {self.video} 작품을 관람하였습니다."
