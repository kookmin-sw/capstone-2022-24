"""Model definition of users application: SocialType, UserManager, User"""
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from mileages.models import Mileage
from users.validators import cell_phone_number_validator, get_nickname_validators


class UserManager(BaseUserManager):
    """Model of managing user object crud"""

    # pylint: disable=R0913
    def create_user(self, nickname, name, email, cell_phone_number, birthday, password=None):
        """Manage to create normal user"""

        if not email:
            raise ValueError("Users must have an email address")

        if not cell_phone_number:
            raise ValueError("Users must have an cell phone number")

        if not birthday:
            raise ValueError("Users must have birthday")

        user = self.model(
            nickname=nickname,
            name=name,
            email=self.normalize_email(email),
            cell_phone_number=cell_phone_number,
            birthday=birthday,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # pylint: disable=R0913
    def create_superuser(self, nickname, name, email, cell_phone_number, birthday, password):
        """Manage to create superuser"""

        user = self.create_user(
            nickname=nickname,
            name=name,
            email=email,
            cell_phone_number=cell_phone_number,
            birthday=birthday,
        )
        user.is_admin = True
        user.is_verified = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """Model of user that use ongot service"""

    nickname = models.CharField(
        max_length=8,
        unique=True,
        validators=get_nickname_validators(),
    )
    name = models.CharField(max_length=30)
    email = models.EmailField(
        max_length=50,
    )
    cell_phone_number = models.CharField(max_length=14, validators=[cell_phone_number_validator])
    # profile_image_url = models.ImageField(blank=True, null=True)
    profile_image_url = models.URLField(blank=True, null=True)
    birthday = models.DateField()
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    total_mileages = models.PositiveIntegerField(default=0)
    withdrawal_date_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    registration_date_time = models.DateTimeField(
        default=timezone.now,
    )
    last_login_date_time = models.DateTimeField(
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "nickname"
    EMAIL_FIELD = "email"
    objects = UserManager()

    REQUIRED_FIELDS = ["email", "name", "cell_phone_number", "birthday"]

    class Meta:
        """Metadata of User model"""

        db_table = "user"
        ordering = ("-registration_date_time",)

    def __str__(self):
        return f"{self.nickname}"

    def has_perm(self, perm, obj=None):
        """Always has perms"""
        return True

    def has_module_perms(self, app_label):
        """Always has module perms"""
        return True

    @property
    def is_staff(self):
        """Isn't normal but admin?"""
        return self.is_admin


@receiver(post_save, sender=Mileage)
def update_user_total_mileages(self, instance: Mileage, created, **kwargs):
    """When mileage record is created, update user total_mileages field with record"""
    if created:
        _user = instance.user
        _user.total_mileages += instance.amount
        _user.save()
