"""Admin settings of mileages application"""
from django.contrib import admin

from .models import Mileage

admin.site.register(Mileage)
