"""Videos App Model Definitions: VideoProvider"""
from django.utils import timezone
from djongo import models
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

    id = models.BigAutoField(
        primary_key=True,
    )
    video_id = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,  # videos 삭제시 같이 삭제
        db_column="videoId",
    )
    provider_id = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        db_column="providerId",
    )
    offer_type = models.CharField(
        max_length=8,
        null=True,
        choices=OFFER_CHOICES,
        db_column="offerType",
    )
    link = models.URLField(
        null=False,
    )
    offer_date = models.DateField(
        default=timezone.now,
        null=True,
        db_column="offerDate",
    )
    deadline = models.DateField(
        default=timezone.now,
        null=False,
    )

    class Meta:
        """DB table naming"""

        db_table = "video_providers"

    def __str__(self):
        return f"{self.video_id}를 제공하는 {self.provider_id}"
