"""Definitions of model about Casts informations : VideoCast"""
from django.db import models
from videos.models import Video


class VideoCast(models.Model):
    """Definition of information about casts who appeared in the video"""

    DEPARTMENT_CHOICE = (
        ("CS", "Cast"),
        ("CR", "Crew"),
        ("SD", "Sound"),
        ("LG", "Lighting"),
        ("PD", "Production"),
        ("AT", "Art"),
        ("ED", "Editing"),
        ("CM", "Costume & Make-Up"),
        ("CR", "Camera"),
        ("DR", "Directing"),
        ("VE", "Visual Effects"),
        ("AC", "Actors"),
        ("WR", "Writing"),
    )
    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=30,
    )
    department = models.CharField(
        max_length=2,
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
        return f"{self.role}역할의 {self.name}"
