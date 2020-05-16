"""Importing the built in Django forms"""
from django import forms

"""Importing the models that we created"""
from studentsece_app.models import StudentECE

class StudentECEForm(forms.ModelForm):
    class Meta:
        model = StudentECE
        exclude = ('user' ,'enrolled')

        #this widgets atttribute changes the field behaviour on the HTML rendering
        widgets = {
            'gender': forms.Select(choices = (
                ('male', 'Male'),
                ('female', 'Female')
                )),

            'birthdate': forms.DateInput(),
            'date_graduated': forms.DateInput(),

            'conditional_subject': forms.Select(choices = (
                ('none', 'Not Applicable'),
                ('mathematics', 'Mathematics'),
                ('geas', 'General Engineering and Applied Sciences'),
                ('electronics', 'Electronics Engineering'),
                ('est', 'Electronic Systems and Technologies'),
            )),

            'review_status': forms.Select(choices = (
                ('first taker', 'First Taker'),
                ('retaker', 'Retaker'),
                ('conditional', 'Conditional')
            )),

            'address': forms.TextInput(),
            'address_contact_person': forms.TextInput(),
            'honors': forms.TextInput(),
            'scholarships': forms.TextInput(),
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
            'conditional_subject': 'Do not change if not conditional.',
        }



        #this widgets atttribute changes the field behaviour on the HTML rendering
