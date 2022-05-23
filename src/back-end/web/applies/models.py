"""Model definition of applies application: BaseApply"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from payments.models import Payment
from providers.models import Provider


class GroupApply(models.Model):
    """Abstract model definition about Common part of apply"""

    FELLOW_CHOICES = (("M", "모임원"), ("L", "모임장"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    apply_date_time = models.DateTimeField(default=timezone.now)
    fellow_type = models.CharField(choices=FELLOW_CHOICES, max_length=1)

    class Meta:
        """Abstract setting obout BaseApply model"""

        unique_together = (
            "user",
            "provider",
        )
        ordering = ("-apply_date_time",)

    def get_apply_date(self):
        """Get apply date from apply_date_time"""
        return self.apply_date_time.date()

    def __str__(self):
        return f"{self.get_fellow_type_display()} 신청 #{self.id} ({self.apply_date_time})"
