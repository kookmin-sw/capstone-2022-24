"""Definitions of model about video providers : VideoProvider"""
from django.db import models
from django.utils import timezone
from providers.models import Provider
from videos.models import Video


class VideoProvider(models.Model):
    """Video OTT Providers information"""

    OFFER_CHOICES = (
        (None, "None_information"),
        ("flatrate", "flatrate"),
        ("rent", "rent"),
        ("buy", "buy"),
    )

    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
    )
    offer_type = models.CharField(
        max_length=8,
        null=True,
        choices=OFFER_CHOICES,
    )
    link = models.URLField()
    offer_date = models.DateField(
        default=timezone.now,
    )
    deadline = models.DateField(
        default=timezone.now,
        null=True,
    )

    class Meta:
        """Metadata for video providers model"""

        db_table = "video_providers"

    def __str__(self):
        return f"{self.video}를 제공"
