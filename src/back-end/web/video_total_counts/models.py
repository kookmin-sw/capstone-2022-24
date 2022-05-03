"""Video Total Counts App Model Definitions: VideoTotalCount"""

from django.db import models
from videos.models import Video


class VideoTotalCount(models.Model):
    """Video Total Counts information about interacting with Users"""

    id = models.BigAutoField(
        primary_key=True,
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        db_column="videoId",
    )
    dibs_count = models.IntegerField(
        null=True,
        default=0,
        db_column="dibsCount",
    )
    watch_count = models.IntegerField(
        null=True,
        default=0,
        db_column="watchCount",
    )
    view_count = models.IntegerField(
        null=True,
        default=0,
        db_column="viewCount",
    )

    class Meta:
        """DB table naming"""

        db_table = "video_total_counts"

    def __str__(self):
        return f"{self.video}의 total Counts"
