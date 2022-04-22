"""Admin settings of recent_views application"""
from django.contrib import admin
from recent_views.models import RecentView

admin.site.register(RecentView)
