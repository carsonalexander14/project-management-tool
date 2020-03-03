from django.contrib import admin

# Register your models here.
from PMT.accounts.models import User, UserProfile, UserManager

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserManager)