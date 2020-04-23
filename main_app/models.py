from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from uuid import uuid4


# Create your models here.
class Topic(models.Model):
    name = models.CharField(primary_key = True, max_length = 100)

class SubTopic(models.Model):
    name = models.CharField(primary_key = True, max_length = 100)
    topic = models.ForeignKey('Topic', on_delete = models.PROTECT)

class Question(models.Model):
    id = models.IntegerField(primary_key = True)
    question = models.CharField(max_length = 2000)
    answer = models.CharField(max_length = 100)
    solution = models.CharField(max_length = 10_000)
    subtopic = models.ForeignKey('Subtopic', on_delete = models.PROTECT)
