from django import forms
from . import models

class HandoutForm(forms.ModelForm):
    class Meta:
        model = models.Handout
        fields = '__all__'
