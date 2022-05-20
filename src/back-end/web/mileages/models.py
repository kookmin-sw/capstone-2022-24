"""Definitions of model for mileages application"""
from django.conf import settings
from django.db import models
from django.utils import timezone


class Mileage(models.Model):
    """Record about User's mileage changes"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    renewal_date_time = models.DateTimeField(
        default=timezone.now,
    )

    class Meta:
        """Metadata for mileage model"""

        db_table = "mileage"

    def __str__(self):
        return f"마일리지 {self.amount}원 갱신"

    # T0D0: 사용자 총 마일리지 갱신
