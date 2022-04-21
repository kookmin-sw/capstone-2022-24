"""Admin settings of star_ratings application"""
from django.contrib import admin

from .models import StarRating

admin.site.register(StarRating)
