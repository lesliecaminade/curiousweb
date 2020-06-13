from django.db import models

# Create your models here.
class Testimony(models.Model):
    name = models.CharField(max_length = 100)
    testimony = models.CharField(max_length = 3000)
    thumbnail = models.ImageField(null = True)
