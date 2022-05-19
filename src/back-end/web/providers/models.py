"""Model definition of providers application: Provider, SubscriptionType, Charge"""
from django.db import models
from django.utils import timezone


def get_logo_prefix():
    """Return prefix to make full logo url"""
    # return f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/providers/logo_images/{settings.STATIC_LOCATION}/"
    return ""  # not use currently


PREFIX = get_logo_prefix()


class Provider(models.Model):
    """Model definition about OTT Providers"""

    NAME_CHOICES = (
        ("NF", "Netflix"),
        ("WC", "Watcha"),
        ("DP", "DisneyPlus"),
        ("TV", "Tving"),
        ("WV", "Wavve"),
        ("AP", "AmazonPrime"),
    )
    tmdb_id = models.PositiveBigIntegerField()
    name = models.CharField(
        max_length=2,
        choices=NAME_CHOICES,
    )
    link = models.URLField(default="https://default_ott_link.com")
    logo_key = models.CharField(max_length=100)

    class Meta:
        """Metadata for provider model"""

        db_table = "provider"

    def __str__(self):
        return f"{self.get_name_display()}"

    @property
    def logo_url(self):
        """Full logo url stored in static storage"""
        return f"{PREFIX + self.logo_key}"


class SubscriptionType(models.Model):
    """Model definition of subscription details"""

    name = models.CharField(primary_key=True, max_length=20)
    number_of_subscribers = models.PositiveSmallIntegerField()
    detail = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        """Metadata for subscription_type model"""

        db_table = "subscription_type"

    def __str__(self):
        return f"{self.name}"


class Charge(models.Model):
    """Model definition of charge details"""

    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
    )
    subscription_type = models.ForeignKey(
        SubscriptionType,
        null=True,
        on_delete=models.SET_NULL,
    )
    service_charge_per_member = models.PositiveIntegerField(default=0)
    subscription_charge_per_member = models.PositiveIntegerField(default=0)
    total_subscription_charge = models.PositiveIntegerField(default=0)
    base_date = models.DateField(default=timezone.now)

    class Meta:
        """Metadata for charge model"""

        db_table = "charge"

    def __str__(self):
        return f"이용료 {self.service_charge_per_member}원/인"
