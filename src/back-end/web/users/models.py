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
    def create_user(self, nickname, email, cell_phone_number, social_type, birthday, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        if not cell_phone_number:
            raise ValueError('Users must have an cell phone number')

        if not birthday:
            raise ValueError('Users must have birthday')

        user = self.model(
            nickname=nickname,
            email=self.normalize_email(email),
            cell_phone_number=cell_phone_number,
            social_type=social_type,
            birthday=birthday
        )

        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, email, cell_phone_number, birthday, password, social_type=None):
        user = self.create_user(
            nickname=nickname,
            email=email,
            cell_phone_number=cell_phone_number,
            birthday=birthday,
            password=password,
            social_type=social_type
        )
        user.is_admin = True
        user.set_password(password)
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
        SocialType,
        default=None,
        db_column="socialTypeId",
        on_delete=models.SET_DEFAULT
    )
    profile_image_url = models.ImageField(
        blank=True,
        null=True,
        db_column="profileImageUrl"
    )
    birthday = models.DateField()
    is_active = models.BooleanField(
        default=True,
        db_column="isActive"
    )
    is_admin = models.BooleanField(
        default=False,
        db_column="isAdmin"
    )
    withdrawal_date_time = models.DateTimeField(
        null=True,
        blank=True,
        db_column="withdrawalDateTime"
    )
    registration_date_time = models.DateTimeField(
        default=timezone.now,
        db_column="registrationDateTime"
    )
    total_mileages = models.PositiveIntegerField(
        default=0,
        db_column="totalMileages"
    )
    last_login = models.DateTimeField(
        blank=True,
        null=True,
        db_column="lastLogin"
    )

    USERNAME_FIELD = "nickname"
    EMAIL_FIELD = "email"
    objects = UserManager()

    REQUIRED_FIELDS = ["email", "cell_phone_number", "birthday"]

    class Meta:
        db_table = "users"
        ordering = ('-registration_date_time',)

    def __str__(self):
        return f"{self.nickname}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
