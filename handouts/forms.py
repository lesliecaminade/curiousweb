from django import forms
from . import models

class HandoutFileForm(forms.ModelForm):
    class Meta:
        model = models.HandoutFile
        exclude = ['is_ece', 'is_ee', 'is_tutorial', 'is_accessible']

class HandoutForm(forms.ModelForm):
    class Meta:
        model = models.Handout
        exclude = ['files', ]
