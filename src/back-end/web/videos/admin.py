"""Admin : Video, VideoDetail"""
from django.contrib import admin
from videos.models import Genre, ProductionCountry, Rating, Video, VideoDetail

admin.site.register(Video)
admin.site.register(VideoDetail)
admin.site.register(Rating)
admin.site.register(Genre)
admin.site.register(ProductionCountry)
