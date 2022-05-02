"""Definitions of model about Casts informations : VideoCast"""
from django.db import models
from videos.models import Video


class VideoCast(models.Model):
    """Definition of information about casts who appeared in the video"""

    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=30,
    )
    department = models.CharField(
        max_length=30,
        null=True,
    )
    role = models.CharField(
        max_length=50,
        null=True,
    )
    character = models.CharField(
        max_length=30,
        null=True,
    )

    class Meta:
        """Metadata for video model"""

        db_table = "video_casts"

    def __str__(self):
        return f"작품 {self.video.title}의 출연진 {self.name}"
