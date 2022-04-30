"""Admin settings of star_ratings application"""
from django.contrib import admin
from star_ratings.models import StarRating

admin.site.register(StarRating)
