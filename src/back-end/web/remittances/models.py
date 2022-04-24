"""Definition of remittances application models: Remittance"""
from django.conf import settings
from django.db import models
from payments.models import Payment


class RemittanceReason(models.Model):
    """Model Definition of remittance reason model that explain service's transfer"""

    id = models.BigAutoField(primary_key=True)
    keyword = models.CharField(max_length=10)
    description = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f"{self.keyword}"


class Remittance(models.Model):
    """Model Definitions of remittance that user receives"""

    STATUS_CHOICES = (("PE", "PENDING"), ("CA", "CANCELED"), ("CO", "COMPLETED"))

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="userId")
    reason = models.ForeignKey(RemittanceReason, default=1, on_delete=models.SET_DEFAULT, db_column="reasonId")
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.SET_NULL, db_column="paymentId")
    amount = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    transfer_date_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"[{self.get_status_display()}] {self.user}님에게 {self.amount}원 송금"
