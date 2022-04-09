from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from djongo import models


class SocialType(models.Model):
    SOCIAL_PLATFORM_CHOICES = (
        ('N', 'Naver'),
        ('G', 'Google'),
    )
    id = models.BigAutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=1,
        choices=SOCIAL_PLATFORM_CHOICES
    )
    logo_key = models.CharField(
        max_length=100,
        db_column="logoKey"
    )

    class Meta:
        db_table = "social_types"

    def __str__(self):
        return f"{self.name}"


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    nickname = models.CharField(
        max_length=8,
        unique=True
    )
    email = models.EmailField(
        max_length=50,
    )
    cell_phone_number = models.CharField(
        max_length=14,
        db_column="cellPhoneNumber"
    )
    social_type = models.ForeignKey(
        model_container=SocialType,
    )
    profile_image_url = models.ImageField(
        blank=True,
        null=True,
    )
    birthday = models.DateField()
    is_active = models.BooleanField(
        default=True
    )
    is_blocked = models.BooleanField(
        default=False,
    )
    withdrawal_date_time = models.DateTimeField(
        null=True,
        default=None,
    )
    registration_date_time = models.DateTimeField(
        default=timezone.now,
    )

    USERNAME_FIELD = "nickname"
    EMAIL_FIELD = "email"
    objects = UserManager()

    REQUIRED_FIELDS = ["nickname", "email", "cell_phone_number", "social_type", "birthday", "registration_date_time"]

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.nickname}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
