from django.utils import timezone
from djongo import models
# from accounts import model


class SocialType(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(
        max_length=10,
        null=False
    ),
    logo_key = models.CharField(
        max_length=30,
        null=False,
    )


class User(models.Model):
    _id = models.ObjectIdField()
    nickname = models.CharField(
        max_length=15,
        null=False
    ),
    email = models.EmailField(
        max_length=50,
        null=False
    )
    cell_phone_number = models.CharField(
        max_length=14,
        null=False,
    ),
    # account = models.ForeignKey(
    #     Account,
    #     null=True,
    #     on_delete=models.CASCADE
    # ),
    social_type = models.EmbeddedField(
        null=False,
        model_container=SocialType,
    ),
    profile_image_url = models.ImageField(
        blank=True,
        null=True,
    ),
    birthday = models.DateField(
        null=True
    ),
    is_blocked = models.BooleanField(
        null=False,
        default=False,
    ),
    registration_date_time = models.DateTimeField(
        null=False,
        default=timezone.now,
    ),
    withdrawal_date_time = models.DateTimeField(
        null=True,
        default=None,
    )
