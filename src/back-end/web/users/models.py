from django.utils import timezone
from djongo import models
# from accounts import model


class social_types(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(
        max_length=10,
        null=False
    ),
    logoKey = models.CharField(
        max_length=30,
        null=False,
    )


class users(models.Model):
    _id = models.ObjectIdField()
    nickname = models.CharField(
        max_length=15,
        null=False
    ),
    email = models.EmailField(
        max_length=50,
        null=False
    )
    cellPhoneNumber = models.CharField(
        max_length=14,
        null=False,
    ),
    # account = models.ForeignKey(
    #     Account,
    #     null=True,
    #     on_delete=models.CASCADE
    # ),
    socialType = models.EmbeddedField(
        null=False,
        model_container=social_types,
    ),
    profileImageUrl = models.ImageField(
        blank=True,
        null=True,
    ),
    birthday = models.DateField(
        null=True
    ),
    isBlocked = models.BooleanField(
        null=False,
        default=False,
    ),
    registrationDateTime = models.DateTimeField(
        null=False,
        default=timezone.now,
    ),
    withdrawalDateTime = models.DateTimeField(
        null=True,
        default=None,
    )
