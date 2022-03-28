from django.utils import timezone
from djongo import models


class payments(models.Model):
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

    _id = models.ObjectIdField()
    amount = models.PositiveIntegerField(
        null=False,
        blank=False,
        default=0
    )
    content = models.CharField(
        null=False,
        blank=False,
        max_length=200
    )
    category = models.CharField(
        null=False,
        blank=False,
        choices=CATEGORY_CHOICES,
        max_length=1
    )
    method = models.CharField(
        null=False,
        blank=False,
        choices=METHOD_CHOICES,
        max_length=10
    )
    status = models.CharField(
        null=False,
        blank=False,
        default='r',
        choices=STATUS_CHOICES,
        max_length=1
    )
    requestDateTime = models.DateTimeField(
        null=False,
        blank=False,
        default=timezone.now
    )
    approvalDateTime = models.DateTimeField(
        null=True,
        blank=True,
    )
