"""Definitions of model about video score evaluated by the user: StarRating"""
from django.conf import settings
from django.utils import timezone
from djongo import models
from videos.models import Video


class StarRating(models.Model):
    """Definition of Star Rating Model"""

    VALUE_CHOICES = (
        (0.5, "0.5"),
        (1.0, "1.0"),
        (1.5, "1.5"),
        (2.0, "2.0"),
        (2.5, "2.5"),
        (3.0, "3.0"),
        (3.5, "3.5"),
        (4.0, "4.0"),
        (4.5, "4.5"),
        (5.0, "5.0"),
    )

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="userId",
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        db_column="videoId",
    )
    value = models.FloatField(
        choices=VALUE_CHOICES,
        default=5,
    )
    date_time = models.DateTimeField(default=timezone.now, db_column="dateTime")

    class Meta:
        """Metadata for StarRating model"""

        db_table = "star_ratings"

    def __str__(self):
        return f"{self.user}님이 {self.video} 작품에 {self.value} 별점을 주었습니다."
