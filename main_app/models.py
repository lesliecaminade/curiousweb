from django.db import models
from django.contrib.auth.models import AbstractUser
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

    def get_absolute_url(self):
        return reverse('main_app:user', kwargs = {'pk':self.pk})

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.CharField(max_length = 100)
    link = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(null = True)

class Announcement(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 2000)
    timestamp = models.DateTimeField(null =  True)

    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField( default = False)
    is_online_class = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
