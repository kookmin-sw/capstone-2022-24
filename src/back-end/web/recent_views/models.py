"""Definitions of model about video history that user recently viewed: RecentView"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from videos.models import Video


class RecentView(models.Model):
    """Definition of history user recently inquired about details"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
    )
    last_view_date_time = models.DateTimeField(default=timezone.now, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        """Metadata for recent_view model"""

        db_table = "recent_view"

    def __str__(self):
        return f"작품 조회 #{self.id}"
