"""Importing the built in Django forms"""
from django import forms

"""Importing the models that we created"""
from main_app.models import (
    Topic,
    Subtopic,
    MultipleChoice,
    Student,
    ElectronicsStudent,
    ElectricalStudent,
    TutorialStudent,
)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('full_name', 'user', 'enrolled')

        #this widgets atttribute changes the field behaviour on the HTML rendering
        widgets = {
            'gender': forms.Select(choices = (
                ('male', 'Male'),
                ('female', 'Female')
                )),

            'course': forms.Select(choices = (
                ('ece', 'Electronics Engineering Review'),
                ('ee', 'Electrical Engineering Review'),
                ('tutorial', 'Tutorial Classes'),
            )),

            'birthdate': forms.DateInput(),
            'date_graduated': forms.DateInput(),
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
            'date_graduated': 'MM/DD/YYYY',

        }
        error_messages = {
            #'name': {
                #'max_length': _("This writer's name is too long."),
            #},
        }

class ElectronicsStudentForm(forms.ModelForm):
    class Meta():
        model = ElectronicsStudent
        exclude = ['student', 'enrolled']

        widgets = {
            'conditional_subject': forms.Select(choices = (
                ('none', 'Not Applicable (First Taker)'),
                ('mathematics', 'Mathematics'),
                ('geas', 'General Engineering and Applied Sciences'),
                ('electronics', 'Electronics Engineering'),
                ('est', 'Electronic Systems and Technologies'),
            )),

            'review_status': forms.Select(choices = (
                ('first taker', 'First Taker'),
                ('retaker', 'Retaker'),
            )),
        }

        labels = {
            'review_status': 'Review Status',
            'conditional_subject': 'Conditional Subject',
        }

        #help_texts = {}

        #error_messages = {}

class ElectricalStudentForm(forms.ModelForm):
    class Meta():
        model = ElectricalStudent
        exclude = ['student', 'enrolled']

        widgets = {
            'review_status': forms.Select(choices = (
                ('first taker', 'First Taker'),
                ('retaker', 'Retaker'),
            )),
        }

        labels = {
            'review_status': 'Review Status',
        }

        #help_texts = {}

        #error_messages = {}

class TutorialStudentForm(forms.ModelForm):
    class Meta():
        model = ElectronicsStudent
        exclude = ['student', 'enrolled']


        #help_texts = {}

        #error_messages = {}
