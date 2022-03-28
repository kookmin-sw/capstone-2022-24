from django.utils import timezone
from djongo import models


class Provider(models.Model):
    NAME_CHOICES = (
        ('NE', 'Netflix'),
        ('WA', 'Watcha'),
        ('DI', 'DisneyPlus'),
        ('TV', 'Tving'),
        ('WA', 'Wavve'),
    )
    id = models.BigAutoField(
        primary_key=True,
    )
    tmdb_id = models.PositiveBigIntegerField(
        db_column="tmdbId"
    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=2,
        choices=NAME_CHOICES,
    )
    logo_key = models.CharField(
        null=False,
        blank=False,
        max_length=200,
        db_column="logoKey"
    )

    class Meta:
        db_table = "providers"

    def __str__(self):
        return f"{self.name}"


class SubscriptionType(models.Model):
    name = models.CharField(
        primary_key=True,
        max_length=20
    )
    number_of_subscribers = models.PositiveSmallIntegerField(
        db_column="numberOfSubscribers"
    )
    detail = models.CharField(
        null=True,
        blank=True,
        max_length=200
    )

    class Meta:
        db_table = "subscription_types"

    def __str__(self):
        return f"{self.name}"


class Charge(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        db_column="provider",
    )
    subscription_type = models.ForeignKey(
        SubscriptionType,
        null=True,
        on_delete=models.SET_NULL,
        db_column="subscriptionType",
    )
    service_charge_per_member = models.PositiveIntegerField(
        null=False,
        default=0,
        db_column="serviceChargePerMember"
    )
    subscription_charge_per_member = models.PositiveIntegerField(
        null=False,
        default=0,
        db_column="subscriptionChargePerMember"
    )
    total_subscription_charge = models.PositiveIntegerField(
        null=False,
        default=0,
        db_column="totalSubscriptionCharge"
    )
    base_date = models.DateField(
        default=timezone.now,
        db_column="baseDate"
    )

    class Meta:
        db_table = "charges"

    def __str__(self):
        return f"[{self.provider}] {self.subscription_type} 요금제"
