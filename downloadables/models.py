from django.db import models


class DownloadableFile(models.Model):
    name = models.CharField(max_length = 100)
    file = models.FileField(upload_to = 'downloadables/files')

    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)

    def __str__(self):
        return self.name

# Create your models here.
class Downloadable(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    image = models.ImageField(null = True, upload_to = 'downloadables/thumbnails')
    files = models.ManyToManyField(DownloadableFile, blank = True)

    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)

    timestamp = models.DateTimeField(null = True)
    def __str__(self):
        return self.name
