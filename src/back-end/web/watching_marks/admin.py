"""Admin settings of watching_marks application"""
from django.contrib import admin

from .models import WatchingMark

admin.site.register(WatchingMark)
