"""Model definition of users application: SocialType, UserManager, User"""
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone


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

        user.set_unusable_password()
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
            password=password,
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """Model of user that use ongot service"""

    nickname = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(
        max_length=50,
    )
    cell_phone_number = models.CharField(max_length=14)
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
