"""Model definition of users application: SocialType, UserManager, User"""
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


class SocialType(models.Model):
    """Model of sns platform that user enters"""

    SOCIAL_PLATFORM_CHOICES = (("N", "Naver"), ("G", "Google"), ("O", "Others"))
    name = models.CharField(max_length=1, choices=SOCIAL_PLATFORM_CHOICES)
    logo_key = models.CharField(max_length=100)

    class Meta:
        """Metadata for social_type model"""

        db_table = "social_type"

    def __str__(self):
        return f"{self.name}"


class UserManager(BaseUserManager):
    """Model of managing user object crud"""

    # pylint: disable=R0913
    def create_user(self, nickname, email, cell_phone_number, social_type, birthday, password=None):
        """Manage to create normal user"""

        if not email:
            raise ValueError("Users must have an email address")

        if not cell_phone_number:
            raise ValueError("Users must have an cell phone number")

        if not birthday:
            raise ValueError("Users must have birthday")

        user = self.model(
            nickname=nickname,
            email=self.normalize_email(email),
            cell_phone_number=cell_phone_number,
            social_type=social_type,
            birthday=birthday,
        )

        user.set_unusable_password()
        user.save(using=self._db)
        return user

    # pylint: disable=R0913
    def create_superuser(self, nickname, email, cell_phone_number, birthday, password, social_type=None):
        """Manage to create superuser"""

        if not social_type:
            social_type = SocialType(1, "O", "Not found")
            social_type.save(using=self._db)
        user = self.create_user(
            nickname=nickname,
            email=email,
            cell_phone_number=cell_phone_number,
            birthday=birthday,
            password=password,
            social_type=social_type,
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, models.Model):
    """Model of user that use ongot service"""

    nickname = models.CharField(max_length=8, unique=True)
    email = models.EmailField(
        max_length=50,
    )
    cell_phone_number = models.CharField(max_length=14)
    social_type = models.ForeignKey(SocialType, default=None, on_delete=models.SET_DEFAULT)
    profile_image_url = models.ImageField(blank=True, null=True)
    birthday = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    total_mileages = models.PositiveIntegerField(default=0)
    withdrawal_date_time = models.DateTimeField(null=True, blank=True)
    registration_date_time = models.DateTimeField(default=timezone.now)
    last_login_date_time = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = "nickname"
    EMAIL_FIELD = "email"
    objects = UserManager()

    REQUIRED_FIELDS = ["email", "cell_phone_number", "birthday"]

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
