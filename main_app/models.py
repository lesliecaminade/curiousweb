from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class ErrorReport(models.Model):
    email = models.EmailField()
    description = models.CharField(max_length = 1000)
    image = models.ImageField(blank = True)


class Topic(models.Model):
    name = models.CharField(max_length = 100, primary_key = True)

class Subtopic(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.PROTECT,
    )
    name = models.CharField(
        max_length = 100,
        primary_key = True,
    )

class MultipleChoice(models.Model):
    author = models.CharField(max_length = 1000, default = 'null')
    question = models.CharField(max_length = 1000)
    image = models.ImageField(blank = True, upload_to = 'mcq_images')
    correct = models.CharField(max_length = 1000)
    wrong_1 = models.CharField(max_length = 1000)
    wrong_2 = models.CharField(max_length = 1000, blank = True)
    wrong_3 = models.CharField(max_length = 1000, blank = True)
    correct_image = models.ImageField(blank = True, upload_to = 'mcq_images')
    wrong_image_1 = models.ImageField(blank = True, upload_to = 'mcq_images')
    wrong_image_2 = models.ImageField(blank = True, upload_to = 'mcq_images')
    wrong_image_3 = models.ImageField(blank = True, upload_to = 'mcq_images')
    solution = models.CharField(max_length = 1000, blank = True)
    subtopic = models.ForeignKey(
        Subtopic,
        on_delete = models.PROTECT,
    )
