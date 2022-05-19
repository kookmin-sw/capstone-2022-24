"""Model definition of group_accounts application: GroupAccount"""
from django.db import models


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
