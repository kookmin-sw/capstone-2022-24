"""Admin : Video, VideoDetail"""
from django.contrib import admin
from videos.models import Gerne, ProductionCountry, Rating, Video, VideoDetail

admin.site.register(Video)
admin.site.register(VideoDetail)
admin.site.register(Rating)
admin.site.register(Gerne)
admin.site.register(ProductionCountry)
