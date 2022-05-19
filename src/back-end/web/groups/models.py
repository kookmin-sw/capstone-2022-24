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

    @property
    def is_waiting_for_watching(self):
        """Waiting for registering group account by leader"""
        return self.get_status() == "Recruited"

    @property
    def is_valid(self):
        """is not expired"""
        _end = self.end_watching_date_time
        return _end is None or _end >= timezone.now()

    @property
    def is_watching(self):
        """is watching or reviewing status"""
        return self.get_status() == "Reviewing" or self.get_status() == "Watching"

    @property
    def can_register_account(self):
        """Check group status is Recruited~"""
        return self.get_status() != "Recruiting" and self.is_valid

    def set_watching_duration(self, start_time, end_time):
        """Change group status and set date time"""
        self.start_watching_date_time = start_time
        self.end_watching_date_time = end_time
        self.save()

    def start_watching_with_duration(self, start_time, end_time):
        """set status to watching and duration from start_time to end_time"""
        self.status = "Watching"
        self.set_watching_duration(start_time, end_time)
        self.save()

    def get_status(self):
        """status details especially in watching duration"""
        if not self.is_valid:
            return "Expired"
        # 관람 중
        if self.status == "Watching":
            # 검토기간 이내일 때
            if self.end_reporting_date_time and self.end_reporting_date_time >= timezone.now():
                return "Reviewing"
        return self.status


@receiver(pre_save, sender=Group)
def initialize_group_account(sender, instance: Group, **kwargs):
    """Create group_account for every new group and attach to the group"""
    # case of creating
    if instance.pk is None:
        # if group doesn't have group_account
        if not hasattr(instance, "group_account"):
            _account = GroupAccount.create_empty_account()
            instance.group_account = _account
