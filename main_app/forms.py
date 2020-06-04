from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms
from . import models

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "password1", "password2")
        model = get_user_model()


class AnnouncementForm(forms.ModelForm):
    class Meta:
        exclude = ['timestamp',]
        model = models.Announcement

        widgets = {
        'type': forms.Select(choices = (
            ('primary', 'Primary'),
            ('secondary', 'Secondary'),
            ('success', 'Success'),
            ('danger', 'Danger'),
            ('warning', 'Warning'),
            ('info', 'Info'),
            ('light', 'Light'),
            ('dark', 'Dark'),

        )),
        }
