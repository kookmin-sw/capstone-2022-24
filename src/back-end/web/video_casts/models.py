"""Definitions of model about Casts informations : VideoCast"""
from django.db import models
from videos.models import Video


class VideoCast(models.Model):
    """Definition of information about casts who appeared in the video"""

    DEPARTMENT_CHOICE = (
        ("Cast"),
        ("Crew"),
        ("Sound"),
        ("Lighting"),
        ("Production"),
        ("Art"),
        ("Editing"),
        ("Costume & Make-Up"),
        ("Camera"),
        ("Directing"),
        ("Visual Effects"),
        ("Actors"),
        ("Writing"),
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=30,
    )
    department = models.CharField(
        max_length=20,
        null=True,
        choices=DEPARTMENT_CHOICE,
    )
    role = models.CharField(
        max_length=50,
        null=True,
    )

    class Meta:
        """Metadata for video model"""

        db_table = "video_casts"

    def __str__(self):
        return f"출연진/제작진 {self.name}"
