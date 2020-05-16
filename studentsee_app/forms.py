"""Importing the built in Django forms"""
from django import forms

"""Importing the models that we created"""
from studentsee_app.models import StudentEE

class StudentEEForm(forms.ModelForm):
    class Meta:
        model = StudentEE
        exclude = ('user' ,'enrolled')

        #this widgets atttribute changes the field behaviour on the HTML rendering
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

            'address' : forms.TextInput(),
            'address_contact_person' : forms.TextInput(),
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
            'address_contact_person' : 'Address'
        }

        help_texts = {
            'birthdate': 'MM/DD/YYYY',
            'date_graduated': 'MM/DD/YYYY',
        }

        #this widgets atttribute changes the field behaviour on the HTML rendering
