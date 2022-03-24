from djongo import models


class User(models.Model):
    _id = models.ObjectIdField()
    nickname = models.CharField(
        max_length=15,
        null=False
    )

