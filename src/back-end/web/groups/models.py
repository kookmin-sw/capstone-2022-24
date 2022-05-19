"""Model definition of groups application: Group"""
import datetime

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from group_accounts.models import GroupAccount
from providers.models import Provider


class Group(models.Model):
    """Model definition of Group composed of leader and members"""

    STATUS_CHOICES = (
        ("Recruiting", "모집중"),
        ("Recruited", "모집완료"),
        ("Reviewing", "검토중"),
        ("Watching", "관람중"),
    )
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    group_account = models.OneToOneField(
        GroupAccount,
        on_delete=models.CASCADE,
        blank=True,
    )
    status = models.CharField(max_length=10, default="Recruiting", choices=STATUS_CHOICES)
    creation_date_time = models.DateTimeField(default=timezone.now)
    start_watching_date_time = models.DateTimeField(null=True, blank=True)
    end_watching_date_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        """Metadata for group model"""

        db_table = "group"

    def __str__(self):
        return f"[{self.get_status_display()}] 모임 #{self.id}"

    @property
    def end_reporting_date_time(self):
        """Calculate deadline datetime of reporting"""
        if self.start_watching_date_time:
            return self.start_watching_date_time + datetime.timedelta(days=3)
        return None


@receiver(pre_save, sender=Group)
def initialize_group_account(sender, instance, **kwargs):
    """Create group_account for every new group and attach to the group"""
    # case of creating
    if instance.pk is None:
        # if group doesn't have group_account
        if not hasattr(instance, "group_account"):
            _account = GroupAccount.create_empty_account()
            instance.group_account = _account
