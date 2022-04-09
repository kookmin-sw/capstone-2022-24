from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from djongo import models
from ..accounts.models import Account


class SocialType(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    ),
    logo_key = models.CharField(
        null=False,
        blank=False,
        max_length=100,
        db_column="logoKey"
    )

    class Meta:
        db_table = "social_types"

    def __str__(self):
        return f"{self.name}"


class User(AbstractBaseUser, models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    nickname = models.CharField(
        max_length=8,
        null=False,
        unique=True
    ),
    email = models.EmailField(
        max_length=50,
        null=False
    ),
    cell_phone_number = models.CharField(
        max_length=14,
        null=False,
        db_column="cellPhoneNumber"
    ),
    account = models.ForeignKey(
        Account,
        null=True,
        on_delete=models.CASCADE
    ),
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

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.nickname}"
