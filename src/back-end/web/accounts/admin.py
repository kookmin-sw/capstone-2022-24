"""Admin configurations of accounts application"""
from accounts.models import Account, Bank
from django.contrib import admin

admin.site.register(Bank)
admin.site.register(Account)
