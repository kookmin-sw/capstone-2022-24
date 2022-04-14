from django.conf import settings
from django.utils import timezone
from djongo import models
from groups.models import Group
from payments.models import Payment


class Fellow(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column="userId"
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        db_column="groupId"
    )
    payment = models.ForeignKey(
        Payment,
        on_delete=models.CASCADE,
        db_column="paymentId"
    )
    will_renew = models.BooleanField(
        default=True,
        db_column="willRenew"
    )
    creation_date_time = models.DateTimeField(
        default=timezone.now,
        db_column="creationDateTime"
    )
    last_modification_date_time = models.DateTimeField(
        default=timezone.now,
        db_column="lastModificationDateTime"
    )
    has_reported = models.BooleanField(
        default=False,
        db_column="hasReported"
    )

    class Meta:
        db_table = "fellows"
        ordering = ('-creation_date_time',)

    def __str__(self):
        return f"[모임 #{self.group.id}] {self.user} 구성원"


class Member(Fellow):
    fellow = models.OneToOneField(
        Fellow,
        parent_link=True,
        on_delete=models.CASCADE,
        related_name='member',
        db_column="fellowId"
    )
    has_reported_leader = models.BooleanField(
        default=False,
        db_column="hasReportedLeader"
    )

    class Meta:
        db_table = "members"

    def __str__(self):
        return f"[모임 #{super().group.id}] {super().user} 모임원"


class Leader(Fellow):
    fellow = models.OneToOneField(
        Fellow,
        parent_link=True,
        on_delete=models.CASCADE,
        related_name='leader',
        db_column="fellowId"
    )

    class Meta:
        db_table = "leaders"

    def __str__(self):
        return f"[모임 #{super().group.id}] {super().user} 모임장"
