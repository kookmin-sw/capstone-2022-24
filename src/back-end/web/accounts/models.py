from djongo import models


class Bank(models.Model):
    _id = models.ObjectIdField()
    code = models.CharField(
        max_length=10,
        null=False
    )
    name = models.CharField(
        max_length=10,
        null=False
    )


class Account(models.Model):
    _id = models.ObjectIdField()
    bank = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
        null=False,
    )
    name = models.CharField(
        max_length=10,
        null=False
    )
