from django import forms
from . import models

class MCQForm(forms.ModelForm):
    class Meta:
        model = models.MCQ
        fields = '__all__'
        widgets = {
            'choice1': forms.RadioSelect,
            'choice2': forms.RadioSelect,
            'choice3': forms.RadioSelect,
            'choice4': forms.RadioSelect,
        }

class CategoryAForm(forms.ModelForm):
    class Meta:
        model = models.CategoryA
        exclude = ('exams', )
