from ..config.settings import base
from djongo import models


class Bank(models.Model):
    id = models.BigAutoField(
        primary_key=True,
    )
    code = models.CharField(
        max_length=10,
        null=False
    )
    name = models.CharField(
        max_length=10,
        null=False
    )

    class Meta:
        db_table = "banks"

    def __str__(self):
        return f"{self.name}"


class Account(models.Model):
    id = models.BigAutoField(
        primary_key=True,
    )
    bank = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
        null=False,
        db_column="bankId",
    )
    user = models.ForeignKey(
        base.AUTH_USER_MODEL,
        null = False,
        on_delete=models.CASCADE,
        db_column="userId"
    )
    name = models.CharField(
        max_length=10,
        null=False
    )

    class Meta:
        db_table = "accounts"

    def __str__(self):
        return f"[{self.bank.name}] {self.name}"
