"""Videos App Model Definitions: Video, VideoDetail"""
from django.db import models


class Video(models.Model):
    """Video information that ott providers support"""

    id = models.BigAutoField(
        primary_key=True,
    )

    class Meta:
        """Metadata for video model"""

        db_table = "video"
