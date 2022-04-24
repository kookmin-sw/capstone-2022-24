"""Definition of user's financial details in accounts application: Account, Bank"""
from django.conf import settings
from django.db import models


class Bank(models.Model):
    """Model Definition of bank in Korea"""

    id = models.BigAutoField(
        primary_key=True,
    )
    code = models.CharField(max_length=10, null=False)
    name = models.CharField(max_length=10, null=False)

    class Meta:
        """Metadata of table"""

        db_table = "bank"

    def __str__(self):
        return f"{self.name}"


class Account(models.Model):
    """Model Definition of account held by user"""

    id = models.BigAutoField(
        primary_key=True,
    )
    bank = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
        null=False,
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, null=False)

    class Meta:
        """Metadata of table"""

        db_table = "account"

    def __str__(self):
        return f"[{self.bank.name}] {self.name}"
