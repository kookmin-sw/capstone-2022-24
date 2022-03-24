from pickle import NONE
from djongo import models
from videos.models import videos

# Create your models here.
class video_total_counts(models.Model):
    videoId= models.ForeignKey(videos, on_delete= None) #얘는... 지우면 안돼지
    dibsCount = models.IntegerField(null=True, default=0)
    watchCount = models.IntegerField(null=True, default=0)
    viewCount = models.IntegerField(null=True, default=0)