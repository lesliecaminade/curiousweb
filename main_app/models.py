from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class Program(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_student = models.BooleanField('student status', default = False)
    is_teacher = models.BooleanField('teacher status', default = False)
    is_enrolled = models.BooleanField('enrolled status', default = False)
    is_premium = models.BooleanField('premium status', default = False)
    is_ece = models.BooleanField('ece status', default = False)
    is_ee = models.BooleanField('ee status', default = False)
    is_tutorial = models.BooleanField('tutorial status', default = False)
    is_online_class = models.BooleanField(default = False)

    exam_credits = models.PositiveSmallIntegerField(default = 0)
    date_created = models.DateField(null = True)

    session_key = models.CharField(max_length = 1000, null = True, blank = True)

    def get_absolute_url(self):
        return reverse('main_app:user', kwargs = {'pk':self.pk})

class Activity(models.Model):
    author = models.ForeignKey(User, on_delete = models.PROTECT, null = True)
    content = models.CharField(max_length = 1000, null = True)
    url = models.CharField(max_length = 1000, null = True)
    timestamp = models.DateTimeField(default = timezone.now)
    is_ece = models.BooleanField('ece status', default = False)
    is_ee = models.BooleanField('ee status', default = False)
    is_tutorial = models.BooleanField('tutorial status', default = False)

    class Meta:
        ordering = ['-pk']

class Announcement(models.Model):
    author = models.ForeignKey(User, on_delete = models.PROTECT, null = True)
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 20000)
    timestamp = models.DateTimeField(null =  True)

    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField( default = False)
    is_online_class = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
