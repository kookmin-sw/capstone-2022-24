from django.utils import timezone
from djongo import models

class providers(models.Model):
    NAME_CHOICES = (
        ('NE', 'Netflix'),
        ('WA', 'Watcha'),
        ('DI', 'DisneyPlus'),
        ('TV', 'Tving'),
        ('WA', 'Wavve'),
    )
    _id = models.ObjectIdField()
    tmdbId = models.PositiveBigIntegerField()
    name = models.CharField(
        null=False,
        blank=False,
        max_length=2,
        choices=NAME_CHOICES,
    )
    logoKey = models.CharField(
        null=False,
        blank=False,
        max_length=200
    )


class subscription_types(models.Model):
    name = models.CharField(
        max_length=10
    )
    numberOfSubscribers = models.PositiveSmallIntegerField()
    detail = models.CharField(
        null=True,
        blank=True,
        max_length=200
    )

    class Meta:
        abstract = True


class charges(models.Model):
    _id = models.ObjectIdField()
    provider = models.ForeignKey(
        providers,
        null=False,
        on_delete=models.CASCADE
    )
    subscriptionType = models.EmbeddedField(
        model_container=subscription_types,
    )
    serviceChargePerMember = models.PositiveIntegerField(
        null=False,
        default=0
    )
    subscriptionChargePerMember = models.PositiveIntegerField(
        null=False,
        default=0
    )
    totalSubscriptionCharge = models.PositiveIntegerField(
        null=False,
        default=0
    )
    baseDate = models.DateField(
        default=timezone.now()
    )
