"""Model definition of group_accounts application: GroupAccount"""
from django.db import models
from django.utils import timezone


class GroupAccount(models.Model):
    """Model definition of account used to share with members in a group"""

    identifier = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    creation_date_time = models.DateTimeField(null=True, blank=True)
    last_modification_date_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        """Metadata for group_account model"""

        db_table = "group_account"

    def __str__(self):
        return f"모임 계정 #{self.id}"

    @property
    def has_registered(self):
        """if leader entered full account information"""
        return self.creation_date_time is not None

    @property
    def can_watch(self):
        """id/pw is not null"""
        return self.identifier and self.password

    @classmethod
    def create_empty_account(cls):
        """Initialize object and return its id"""
        return cls.objects.create()

    def save(self, *args, **kwargs):
        """Save group account id/pw"""
        # modify id/pw (already fully registered at least once)
        if self.has_registered:
            self.last_modification_date_time = timezone.now()
        # idd/pw not fulfilled before
        else:
            # now fulfilled
            _id_filled = kwargs.get("identifier") or self.identifier
            _pw_filled = kwargs.get("password") or self.password
            if _id_filled and _pw_filled:
                self.creation_date_time = timezone.now()
        super().save()
