from django import forms
from . import models

class DownloadableFileForm(forms.ModelForm):
    class Meta:
        model = models.DownloadableFile
        exclude = ['is_ece', 'is_ee', 'is_tutorial', 'is_accessible']

class DownloadableForm(forms.ModelForm):
    class Meta:
        model = models.Downloadable
        exclude = ['files', 'timestamp',]
