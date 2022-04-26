"""Definition of remittances application models: Remittance"""
from django.conf import settings
from django.db import models
from payments.models import Payment


class RemittanceReason(models.Model):
    """Model Definition of remittance reason model that explain service's transfer"""

    keyword = models.CharField(max_length=10)
    description = models.CharField(null=True, blank=True, max_length=100)

    class Meta:
        """Metadata for remittance_reason model"""

        db_table = "remittance_reason"

    def __str__(self):
        return f"{self.keyword}"


class Remittance(models.Model):
    """Model Definitions of remittance that user receives"""

    STATUS_CHOICES = (("PE", "PENDING"), ("CA", "CANCELED"), ("CO", "COMPLETED"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reason = models.ForeignKey(RemittanceReason, default=1, on_delete=models.SET_DEFAULT)
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    transfer_date_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        """Metadata for remittance model"""

        db_table = "remittance"

    def __str__(self):
        return f"[{self.get_status_display()}] {self.amount}원 송금내역"
