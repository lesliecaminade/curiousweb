from django import forms
from . import models


class ExamForm(forms.ModelForm):
    class Meta:
        model = models.Exam
        exclude = ['answer_sheets', 'answer_key', 'files', 'timestamp',]

class FileForm(forms.ModelForm):
    class Meta:
        model = models.ExamFile
        exclude = ['is_ece', 'is_ee', 'is_tutorial', 'is_accessible']
