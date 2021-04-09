from django.contrib import admin

# Register your models here.
from accounts.models import User, Skill


admin.site.register([User, Skill])
