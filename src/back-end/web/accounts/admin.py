"""Admin configurations of accounts application"""
from django.contrib import admin

from .models import Account, Bank

admin.site.register(Bank)
admin.site.register(Account)
