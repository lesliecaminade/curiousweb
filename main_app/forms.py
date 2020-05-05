"""Importing the built in Django forms"""
from django import forms

"""Importing the models that we created"""
from main_app.models import (
Topic, Subtopic, MultipleChoice,
)


class QuestionCustomizeForm(forms.Form):
    topic = forms.CharField(max_length = 200)
    subtopic = forms.CharField(max_length = 200)
