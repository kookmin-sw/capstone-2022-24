from django.db import models
from django.forms import URLField
from videos.models import videos

# Create your models here.
class video_providers(models.Model):
    videoId= models.ForeignKey(videos)
    offerType = models.CharField(null=True)
    link = models.URLField(null=False)
    offerDate = models.DateField(null=True)
    deadline = models.DateField(null=False)

