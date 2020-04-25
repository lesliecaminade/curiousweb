from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from uuid import uuid4


# Create your models here.
class ErrorReport(models.Model):
    email = models.EmailField()
    description = models.CharField(max_length = 1000)
    image = models.ImageField()
