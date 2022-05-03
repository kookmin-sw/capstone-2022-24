"""Admin settings of watching_marks application"""
from django.contrib import admin
from watching_marks.models import WatchingMark

admin.site.register(WatchingMark)
