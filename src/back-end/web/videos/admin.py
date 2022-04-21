"""Admin settings of video"""
from django.contrib import admin
from videos.models import Video

admin.site.register(Video)
