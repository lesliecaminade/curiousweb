from django.db import models
from django.utils import timezone
from django.urls import reverse
from main_app.models import User
from uuid import uuid4

class StudentEE(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    #full_name = models.CharField(max_length = 200, primary_key = True) #this would just be simply firstname_lastname
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100)
    birthdate = models.DateField() #this is required
    address = models.TextField(max_length = 1000)
    religion = models.CharField(max_length = 50, blank = True)
    mobile_number = models.CharField(max_length = 100)
    facebook_username = models.CharField(max_length = 100, blank= True)
    email = models.EmailField()
    gender = models.CharField(max_length = 100)
    school = models.CharField(max_length = 100)
    date_graduated = models.DateField(blank = True, null = True) #date graduated is optional

    honors = models.TextField(max_length = 1000, blank = True)
    officer_position = models.CharField(max_length = 100, blank = True)
    scholarships = models.TextField(max_length = 1000, blank = True)

    first_name_contact_person = models.CharField(max_length=100)
    last_name_contact_person = models.CharField(max_length=100)
    middle_name_contact_person = models.CharField(max_length=100, blank = True)
    address_contact_person = models.CharField(max_length=1000)
    mobile_number_contact_person = models.CharField(max_length = 1000)

    review_status = models.CharField(max_length = 50)
    id_picture = models.ImageField(blank = True)
    payment_picture = models.ImageField()
    enrolled = models.BooleanField(default = False)

    def get_absolute_url(self):
        return reverse("studentsee_app:detail",kwargs={'pk':self.pk})
