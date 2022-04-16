"""Definitions of model for mileages application"""
from django.conf import settings
from django.db import models
from django.utils import timezone


class Mileage(models.Model):
    """Record about User's mileage changes"""

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="userId")
    amount = models.IntegerField(default=0)
    renewal_date_time = models.DateTimeField(default=timezone.now, db_column="renewalDateTime")

    class Meta:
        """Meta data about Mileage model"""

        db_table = "mileages"

    def __str__(self):
        return f"{self.user}님의 마일리지 {self.amount}원 갱신"

    # T0D0: 사용자 총 마일리지 갱신
