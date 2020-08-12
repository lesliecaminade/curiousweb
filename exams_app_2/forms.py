from django import forms
from . import models


class ExamForm(forms.ModelForm):
    class Meta:
        model = models.Exam
        fields = ['name', 'description', 'is_ece', 'is_ee', 'is_tutorial', 'thumbnail']

class FileForm(forms.ModelForm):
    class Meta:
        model = models.ExamFile
        exclude = ['is_ece', 'is_ee', 'is_tutorial', 'is_accessible']

class RepeatForm(forms.ModelForm):
    class Meta:
        model = models.Exam
        fields = ['name', 'description']

        labels = {
            'name': 'New Name',
            'description': 'New Description'
        }

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = models.Submission
        exclude = ['timestamp', 'author', 'comments']

            # author = models.ForeignKey(User, on_delete = models.PROTECT)
            # title = models.CharField(max_length=250)
            # text = models.TextField(max_length=5000, blank=True)
            # timestamp = models.DateTimeField(default=timezone.now)
            # image = models.ImageField(blank = True, upload_to = 'discussion/submissions')
            # thumbnail = models.ImageField(blank = True, upload_to = 'discussion/thumbnails')
            # comments = models.ManyToManyField(Comment)

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        exclude = ['timestamp', 'author', 'comments', 'title']

            # author = models.ForeignKey(User, on_delete = models.PROTECT)
            # #title = models.CharField(max_length=250)
            # text = models.TextField(max_length=5000, blank=True)
            # timestamp = models.DateTimeField(default=timezone.now)
            # image = models.ImageField(blank = True, upload_to = 'discussion/comments')
            # thumbnail = models.ImageField(blank = True, upload_to = 'discussion/thumbnails')
