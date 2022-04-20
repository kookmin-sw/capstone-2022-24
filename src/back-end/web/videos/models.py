"""Videos App Model Definitions: Video, VideoDetail"""
from djongo import models


class Video(models.Model):
    """Video information that ott providers support"""

    id = models.BigAutoField(
        primary_key=True,
    )
