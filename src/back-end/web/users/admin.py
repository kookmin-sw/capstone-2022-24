from django.contrib import admin
from .models import User, SocialType

admin.site.register(User)
admin.site.register(SocialType)
