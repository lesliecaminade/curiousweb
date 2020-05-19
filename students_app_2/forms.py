"""Importing the built in Django forms"""
from django import forms

"""Importing the models that we created"""
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        exclude = ('user' ,'enrolled')

        widgets = {
            'gender': forms.Select(choices = (
                ('male', 'Male'),
                ('female', 'Female')
                )),

            'birthdate': forms.DateInput(),
            'date_graduated': forms.DateInput(),


            'review_status': forms.Select(choices = (
                ('first taker', 'First Taker'),
                ('retaker', 'Retaker'),
            )),
            #remove the above for tutorial and edit for ee

            'address': forms.TextInput(),
            'address_contact_person': forms.TextInput(),
            'honors': forms.TextInput(), #remove for tutorial
            'scholarships': forms.TextInput(), #remove for tutorial
        }

        labels = {
            'birthdate': 'Birthday',
            'id_picture': 'ID picture',
            'payment_picture': 'Proof of Payment picture',
            'first_name_contact_person': 'First Name',
            'last_name_contact_person': 'Last Name',
            'middle_name_contact_person': 'Middle Name',
            'mobile_number_contact_person': 'Mobile Number',
            'course': 'Program',
        }

        help_texts = {
            'birthdate': 'MM/DD/YYYY',
            'date_graduated': 'MM/DD/YYYY', #remove for tutorial
        }
