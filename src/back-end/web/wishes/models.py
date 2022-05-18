"""Wishes App Model Definitions: Wish"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from video_total_counts.views import decrease_wish_count, increase_wish_count
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
        unique_together = (
            "user",
            "video",
        )

    def __str__(self):
        return f"찜 #{self.id}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        increase_wish_count(self.video)

    def delete(self, using=None, keep_parents=False):
        super().delete(using, keep_parents)
        decrease_wish_count(self.video)
