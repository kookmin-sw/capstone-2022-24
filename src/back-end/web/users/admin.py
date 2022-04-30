"""Admin configurations of users application"""
from django.contrib import admin
from users.models import SocialType, User

admin.site.register(User)
admin.site.register(SocialType)
