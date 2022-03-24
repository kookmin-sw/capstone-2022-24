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
        db_column="cellPhoneNumber"
    ),
    # account = models.ForeignKey(
    #     Account,
    #     null=True,
    #     on_delete=models.CASCADE
    # ),
    social_type = models.EmbeddedField(
        null=False,
        model_container=SocialType,
        db_column="socialType"
    ),
    profile_image_url = models.ImageField(
        blank=True,
        null=True,
        db_column="profileImageUrl"
    ),
    birthday = models.DateField(
        null=True
    ),
    is_blocked = models.BooleanField(
        null=False,
        default=False,
        db_column="isBlocked"
    ),
    registration_date_time = models.DateTimeField(
        null=False,
        default=timezone.now,
        db_column="registrationDateTime"
    ),
    withdrawal_date_time = models.DateTimeField(
        null=True,
        default=None,
        db_column="withdrawalDateTime"
    )
