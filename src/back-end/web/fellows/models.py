"""Models of fellow application: Fellow, Member, Leader"""
from django.conf import settings
from django.utils import timezone
from djongo import models
from groups.models import Group
from payments.models import Payment


class Fellow(models.Model):
    """User included in a specific group"""

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="userId")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_column="groupId")
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, db_column="paymentId")
    will_renew = models.BooleanField(default=True, db_column="willRenew")
    creation_date_time = models.DateTimeField(default=timezone.now, db_column="creationDateTime")
    last_modification_date_time = models.DateTimeField(default=timezone.now, db_column="lastModificationDateTime")
    has_reported = models.BooleanField(default=False, db_column="hasReported")

    class Meta:
        """Metadata of fellow model"""

        db_table = "fellows"
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
    fellow = models.OneToOneField(Fellow, on_delete=models.CASCADE, related_name="member", db_column="fellowId")
    has_reported_leader = models.BooleanField(default=False, db_column="hasReportedLeader")

    class Meta:
        """Metadata of member model"""

        db_table = "members"

    def __str__(self):
        return f"{self.fellow} 모임원"


class Leader(models.Model):
    """User that has to pay OTT among fellows"""

    id = models.BigAutoField(primary_key=True)
    fellow = models.OneToOneField(Fellow, on_delete=models.CASCADE, related_name="leader", db_column="fellowId")

    class Meta:
        """Metadata of leader model"""

        db_table = "leaders"

    def __str__(self):
        return f"{self.fellow} 모임장"
