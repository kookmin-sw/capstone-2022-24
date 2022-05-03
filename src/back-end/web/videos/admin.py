"""Admin : Video, VideoDetail"""
from django.contrib import admin

from .models import Video, VideoDetail

admin.site.register(Video)
admin.site.register(VideoDetail)
