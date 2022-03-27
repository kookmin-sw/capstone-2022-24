from djongo import models


class banks(models.Model):
    _id = models.ObjectIdField()
    code = models.CharField(
        max_length=10,
        null=False
    )
    name = models.CharField(
        max_length=10,
        null=False
    )


class accounts(models.Model):
    _id = models.ObjectIdField()
    bank = models.ForeignKey(
        banks,
        on_delete=models.CASCADE,
        null=False,
    )
    name = models.CharField(
        max_length=10,
        null=False
    )
