"""Model Definition of payments application: Payment"""
from django.db import models
from django.utils import timezone


class Payment(models.Model):
    """Definition of Payment details model for payments application"""

    CATEGORY_CHOICES = (("N", "NORMAL"), ("B", "BILLING"), ("C", "CONNECTPAY"))

    METHOD_CHOICES = (
        ("C", "CARD"),
        ("VA", "VIRTUAL_ACCOUNT"),
        ("CP", "CELL_PHONE"),
        ("AT", "ACCOUNT_TRANSFER"),
        ("V", "VOUCHER"),
    )

    STATUS_CHOICES = (
        ("R", "READY"),
        ("I", "IN_PROGRESS"),
        ("W", "WAITING_FOR_DEPOSIT"),
        ("D", "DONE"),
        ("C", "CANCELED"),
        ("P", "PARTIAL_CANCELED"),
        ("A", "ABORTED"),
        ("E", "EXPIRED"),
    )

    amount = models.PositiveIntegerField(
        default=0,
    )
    content = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    method = models.CharField(choices=METHOD_CHOICES, max_length=2)
    status = models.CharField(default="R", choices=STATUS_CHOICES, max_length=1)
    request_date_time = models.DateTimeField(default=timezone.now, format="%Y-%m-%d %H:%M:%S")
    approval_date_time = models.DateTimeField(null=True, blank=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        """Metadata for payment model"""

        db_table = "payment"

    def __str__(self):
        return f"[{self.get_status_display()}] {self.amount}원 결제 내역"
