from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Downloadable)
admin.site.register(models.DownloadableFile)
