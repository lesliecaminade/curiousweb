from django.db import models


class HandoutFile(models.Model):
    name = models.CharField(max_length = 100)
    file = models.FileField()

    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)

    def __str__(self):
        return self.name

# Create your models here.
class Handout(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    image = models.ImageField(null = True)
    files = models.ManyToManyField(HandoutFile, blank = True)

    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)

    def __str__(self):
        return self.name
