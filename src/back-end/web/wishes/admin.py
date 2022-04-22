"""Admin settings of wishes application"""
from django.contrib import admin
from wishes.models import Wish

admin.site.register(Wish)
