from django.contrib import admin

# Register your models here.
from . import models
from django.contrib.auth.admin import UserAdmin

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Activity)
admin.site.register(models.Announcement)
