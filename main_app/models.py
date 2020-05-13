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
        on_delete=models.CASCADE,
        null = True,
        blank = True,
    )
    name = models.CharField(max_length = 100, primary_key = True)

class Subsubtopic(models.Model):
    subtopic = models.ForeignKey(
        Subtopic,
        on_delete = models.CASCADE,
        null = True,
        blank = True,
    )
    name = models.CharField(max_length = 100, primary_key = True)

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

    topic = models.ForeignKey(
        Topic,
        on_delete = models.PROTECT,
        null = True,
        blank = True,
    )

    subtopic = models.ForeignKey(
        Subtopic,
        on_delete = models.PROTECT,
        null = True,
        blank = True,
    )

    subsubtopic = models.ForeignKey(
        Subsubtopic,
        on_delete = models.PROTECT,
        null = True,
        blank = True,
    )

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.PROTECT, null = True)
    #full_name = models.CharField(max_length = 200, primary_key = True) #this would just be simply firstname_lastname
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100)
    birthdate = models.DateField()
    address = models.TextField(max_length = 1000)
    religion = models.CharField(max_length = 50, blank = True)
    mobile_number = models.CharField(max_length = 100)
    facebook_username = models.CharField(max_length = 100, blank= True)
    gender = models.CharField(max_length = 100)
    course = models.CharField(max_length = 100)
    school = models.CharField(max_length = 100)
    date_graduated = models.DateField(blank = True)
    honors = models.TextField(max_length = 1000, blank = True)
    officer_position = models.CharField(max_length = 100, blank = True)
    scholarships = models.TextField(max_length = 1000, blank = True)
    email = models.EmailField()
    first_name_contact_person = models.CharField(max_length=100)
    last_name_contact_person = models.CharField(max_length=100)
    middle_name_contact_person = models.CharField(max_length=100, blank = True)
    address_contact_person = models.CharField(max_length=1000)
    mobile_number_contact_person = models.CharField(max_length = 1000)


class ElectronicsStudent(models.Model):
    student = models.ForeignKey(Student, on_delete = models.PROTECT, null = True)
    review_status = models.CharField(max_length = 50)
    conditional_subject = models.CharField(max_length = 50)
    id_picture = models.ImageField(blank = True, upload_to = 'id_pictures')
    payment_picture = models.ImageField(upload_to = 'payment_pictures')
    enrolled = models.BooleanField(default = False)

class ElectricalStudent(models.Model):
    student = models.ForeignKey(Student, on_delete = models.PROTECT, null = True)
    review_status = models.CharField(max_length = 50)
    id_picture = models.ImageField(blank = True, upload_to = 'id_pictures')
    payment_picture = models.ImageField(upload_to = 'payment_pictures')
    enrolled = models.BooleanField(default = False)

class TutorialStudent(models.Model):
    student = models.ForeignKey(Student, on_delete = models.PROTECT, null = True)
    id_picture = models.ImageField(blank = True, upload_to = 'id_pictures')
    payment_picture = models.ImageField(upload_to = 'payment_pictures')
    enrolled = models.BooleanField(default = False)
