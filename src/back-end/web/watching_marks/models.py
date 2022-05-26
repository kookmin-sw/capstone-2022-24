"""Definitions of watching mark models: WatchingMark"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from video_total_counts.views import (
    decrease_watching_mark_count,
    increase_watching_mark_count,
)
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
    date_time = models.DateTimeField(
        default=timezone.now,
    )

    class Meta:
        """Metadata for watching_mark model"""

        db_table = "watching_mark"
        unique_together = (
            "user",
            "video",
        )

    def __str__(self):
        return f"작품 관람 #{self.id}"

    @property
    def get_date(self):
        """Get date from date_time field"""
        return self.date_time.date()

    @property
    def get_time(self):
        """Get time from date_time field"""
        return self.date_time.time()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        increase_watching_mark_count(self.video)

    def delete(self, using=None, keep_parents=False):
        super().delete(using, keep_parents)
        decrease_watching_mark_count(self.video)
