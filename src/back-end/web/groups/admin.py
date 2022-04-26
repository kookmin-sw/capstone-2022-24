"""Admin configurations of groups application"""
from django.contrib import admin
from groups.models import Group

admin.site.register(Group)
