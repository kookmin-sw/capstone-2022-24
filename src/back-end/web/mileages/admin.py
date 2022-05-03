"""Admin settings of mileages application"""
from django.contrib import admin
from mileages.models import Mileage

admin.site.register(Mileage)
