"""Model definition of group_accounts application: GroupAccount"""
from django.db import models
from django.utils import timezone


class GroupAccount(models.Model):
    """Model definition of account used to share with members in a group"""

    identifier = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    creation_date_time = models.DateTimeField(null=True, blank=True)
    last_modification_date_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        """Metadata for group_account model"""

        db_table = "group_account"

    def __str__(self):
        return f"모임 계정 #{self.id}"

    @classmethod
    def create_empty_account(cls):
        """Initialize object and return its id"""
        return cls.objects.create()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """Save group account id/pw"""
        # modify id/pw
        if self.identifier and self.password:
            self.last_modification_date_time = timezone.now()
        # register new id/pw
        else:
            # TODO: id/pw 둘다 입력해야 등록일시에 추가
            if update_fields:
                if ("identifier" in update_fields and self.password) or (
                    "password" in update_fields and self.identifier
                ):
                    self.creation_date_time = timezone.now()
        super().save(force_insert, force_update, using, update_fields)
