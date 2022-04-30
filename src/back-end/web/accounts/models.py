"""Definition of user's financial details in accounts application: Account, Bank"""
from django.conf import settings
from django.db import models


class Bank(models.Model):
    """Model Definition of bank in Korea"""

    code = models.CharField(max_length=10)
    name = models.CharField(max_length=10)

    class Meta:
        """Metadata of table"""

        db_table = "bank"

    def __str__(self):
        return f"{self.name}"


class Account(models.Model):
    """Model Definition of account held by user"""

    bank = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    class Meta:
        """Metadata of table"""

        db_table = "account"

    def __str__(self):
        return f"예금주: {self.name}"
