from django.db import models

# Create your models here.
class Handout(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    image = models.ImageField(null = True)
    file = models.FileField(null = True)

    is_ece = models.BooleanField()
    is_ee = models.BooleanField()
    is_tutorial = models.BooleanField()
    is_accessible = models.BooleanField()

    def __str__(self):
        return self.name
