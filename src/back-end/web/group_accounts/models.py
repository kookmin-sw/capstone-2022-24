from django.db import models
from django.utils import timezone


class GroupAccount(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    identifier = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    password = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    creation_date_time = models.DateTimeField(
        null=True,
        blank=True,
        db_column="creationDateTime"
    )
    last_modification_date_time = models.DateTimeField(
        null=True,
        blank=True,
        db_column="lastModificationDateTime"
    )

    class Meta:
        db_table = "group_accounts"

    def __str__(self):
        return f"[{self.id}] 최종 변경일시: {self.last_modification_date_time}"
