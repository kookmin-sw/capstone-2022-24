from django.conf import settings
from django.utils import timezone
from djongo import models
from ..payments.models import Payment
from ..providers.models import Provider


class Apply(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=False,
        on_delete=models.CASCADE,
        db_column="userId"
    )
    payment = models.ForeignKey(
        Payment,
        null=False,
        on_delete=models.CASCADE,
        db_column="paymentId"
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        db_column="providerId"
    )
    apply_date_time = models.DateTimeField(
        default=timezone.now,
        db_column="applyDateTime"
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"[{self.provider.name}] {self.user.name}님의 구성원 신청"
