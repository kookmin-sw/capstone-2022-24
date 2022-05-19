"""Definitions of model about video score evaluated by the user: StarRating"""
from django.conf import settings
from django.db import models
from django.utils import timezone
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

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
    )
    value = models.FloatField(
        choices=VALUE_CHOICES,
        default=5,
    )
    date_time = models.DateTimeField(default=timezone.now, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        """Metadata for star_rating model"""

        db_table = "star_rating"

    def __str__(self):
        return f"{self.value}/5.0점 #{self.id}"
