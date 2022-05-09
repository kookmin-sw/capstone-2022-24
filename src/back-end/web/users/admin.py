"""Admin configurations of users application"""
from django.contrib import admin
from users.models import User

admin.site.register(User)
