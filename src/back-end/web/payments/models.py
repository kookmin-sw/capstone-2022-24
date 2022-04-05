from django.utils import timezone
from djongo import models


class Payment(models.Model):
    CATEGORY_CHOICES = (
        ('n', 'NORMAL'),
        ('b', 'BILLING'),
        ('c', 'CONNECTPAY')
    )

    METHOD_CHOICES = (
        ('Card', '카드'),
        ('Virtual', '가상계좌'),
        ('Phone', '휴대폰'),
        ('Transfer', '계좌이체'),
        ('Voucher', '상품권')
    )

    STATUS_CHOICES = (
        ('r', 'READY'),
        ('i', 'IN_PROGRESS'),
        ('w', 'WAITING_FOR_DEPOSIT'),
        ('d', 'DONE'),
        ('c', 'CANCELED'),
        ('p', 'PARTIAL_CANCELED'),
        ('a', 'ABORTED'),
        ('e', 'EXPIRED')
    )

    id = models.BigAutoField(
        primary_key=True
    )
    amount = models.PositiveIntegerField(
        default=0,
    )
    content = models.CharField(
        max_length=200
    )
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=1
    )
    method = models.CharField(
        choices=METHOD_CHOICES,
        max_length=10
    )
    status = models.CharField(
        default='r',
        choices=STATUS_CHOICES,
        max_length=1
    )
    request_date_time = models.DateTimeField(
        default=timezone.now,
        db_column="requestDateTime"
    )
    approval_date_time = models.DateTimeField(
        null=True,
        blank=True,
        db_column="approvalDateTime"
    )

    class Meta:
        db_table = "payments"

    def __str__(self):
        return f"[{self.id}] {self.content}"
