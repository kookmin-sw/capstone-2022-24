"""Definitions of model about Counting user's video related interacting information : VideoTotalCount"""
from annoying.fields import AutoOneToOneField
from django.db import models
from videos.models import Video


class VideoTotalCount(models.Model):
    """Definition of video total count information about interacting with Users"""

    MAX_COUNT_LIMIT = 2147483647

    video = AutoOneToOneField(
        Video,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    wish_count = models.PositiveIntegerField(
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

    def increase_wish_count(self):
        """Increase wish count"""
        if self.wish_count < self.MAX_COUNT_LIMIT:
            self.wish_count += 1

    def decrease_wish_count(self):
        """Decrease wish count"""
        if self.wish_count > 0:
            self.wish_count -= 1

    def increase_watch_count(self):
        """Increase wish count"""
        if self.watch_count < self.MAX_COUNT_LIMIT:
            self.watch_count += 1

    def decrease_watch_count(self):
        """Decrease wish count"""
        if self.watch_count > 0:
            self.watch_count -= 1

    def increase_view_count(self):
        """Increase wish count"""
        if self.view_count < self.MAX_COUNT_LIMIT:
            self.view_count += 1

    def decrease_view_count(self):
        """Decrease wish count"""
        if self.view_count > 0:
            self.view_count -= 1
