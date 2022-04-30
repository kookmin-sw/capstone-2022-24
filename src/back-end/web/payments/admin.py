"""Admin configuration of payments application"""
from django.contrib import admin
from payments.models import Payment

admin.site.register(Payment)
