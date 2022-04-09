from djongo import models
from videos.models import Videos
from providers.models import Provider
from django.utils import timezone


class VideoProviders(models.Model):
    OFFER_CHOICES = (
        (None, 'None_information'),
        ('flatrate', 'flatrate'),
        ('rent', 'rent'),
        ('buy', 'buy'),
    )

    id = models.BigAutoField(
        primary_key=True,
    )
    video_id= models.ForeignKey(
        Videos,
        on_delete=models.CASCADE, #videos 삭제시 같이 삭제
        db_column= "videoId",
    )
    provider_id=models.ForeignKey(
        Provider,
        on_delete= None,
        db_column= "providerId",
    )
    offer_type = models.CharField(
        max_length=8,
        null=True,
        choices=OFFER_CHOICES,
        db_column='offerType',
    )
    link = models.URLField(
        null=False,
    )
    offer_date = models.DateField(
        default=timezone.now,
        null=True,
        db_column='offerDate',
    )
    deadline = models.DateField(
        default=timezone.now,
        null=False,
    )
