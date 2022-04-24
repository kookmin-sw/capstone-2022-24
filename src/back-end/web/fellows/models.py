"""Models of fellow application: Fellow, Member, Leader"""
from django.conf import settings
from django.db import models
from django.utils import timezone
from groups.models import Group
from payments.models import Payment


class Fellow(models.Model):
    """User included in a specific group"""

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    will_renew = models.BooleanField(default=True)
    creation_date_time = models.DateTimeField(default=timezone.now)
    last_modification_date_time = models.DateTimeField(default=timezone.now)
    has_reported = models.BooleanField(default=False)

    class Meta:
        """Metadata of fellow model"""

        db_table = "fellow"
        ordering = ("-creation_date_time",)
        unique_together = (
            "user",
            "group",
        )

    def __str__(self):
        return f"{self.group}: {self.user}"


class Member(models.Model):
    """User that waits for leader to pay OTT among fellows"""

    id = models.BigAutoField(primary_key=True)
    fellow = models.OneToOneField(Fellow, on_delete=models.CASCADE, related_name="member")
    has_reported_leader = models.BooleanField(default=False)

    class Meta:
        """Metadata for member model"""

        db_table = "member"

    def __str__(self):
        return f"{self.fellow} 모임원"


class Leader(models.Model):
    """User that has to pay OTT among fellows"""

    id = models.BigAutoField(primary_key=True)
    fellow = models.OneToOneField(Fellow, on_delete=models.CASCADE, related_name="leader")

    class Meta:
        """Metadata for leader model"""

        db_table = "leader"

    def __str__(self):
        return f"{self.fellow} 모임장"
