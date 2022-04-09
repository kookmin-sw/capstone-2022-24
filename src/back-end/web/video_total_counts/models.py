from djongo import models
from videos.models import Videos

class VideoTotalCounts(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    video_id= models.ForeignKey(
        Videos,
        on_delete= None,
        db_column="videoId"
    )
    dibs_count = models.IntegerField(
        null=True,
        default=0,
        db_column="dibsCount"
    )
    watch_count = models.IntegerField(
        null=True,
        default=0,
        db_column="watchCount"
    )
    view_count = models.IntegerField(
        null=True,
        default=0,
        db_column="viewCount",
    )

    class Meta:
        db_table = "video_total_counts"

    def __str__(self):
        return f"{self.name}"
