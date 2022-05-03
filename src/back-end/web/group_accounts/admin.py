"""Admin configuration of group_accounts application"""
from django.contrib import admin
from group_accounts.models import GroupAccount

admin.site.register(GroupAccount)
