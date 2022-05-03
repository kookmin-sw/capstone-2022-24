"""Definitions of model about Counting user's video related interacting information : VideoTotalCount"""

from django.db import models
from videos.models import Video


class VideoTotalCount(models.Model):
    """Definition of video total count information about interacting with Users"""

    video = models.OneToOneField(
        Video,
        on_delete=models.CASCADE,
    )
    dibs_count = models.PositiveIntegerField(
        null=True,
        default=0,
    )
    watch_count = models.PositiveIntegerField(
        null=True,
        default=0,
    )
    view_count = models.PositiveIntegerField(
        null=True,
        default=0,
    )

    class Meta:
        """Metadata for video total count model"""

        db_table = "video_total_counts"

    def __str__(self):
        return f"{self.video.title}의 total Counts"
