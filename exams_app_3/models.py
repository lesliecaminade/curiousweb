from django.db import models
from main_app.models import User
from django.urls import reverse_lazy, reverse

class Choice(models.Model):
    content = models.CharField(max_length = 1000)
    correct = models.BooleanField()
    image = models.ImageField(null = True, blank = True, upload_to = 'exams_app_3/choice')

    def __str__(self):
        return content

class MCQAccessCount(models.Model):
    count = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user4')

class MCQ(models.Model):
    question = models.TextField(max_length = 1000, default = '', null = True, blank = True)
    choices = models.ManyToManyField(Choice)
    image = models.ImageField(blank = True, null = True, upload_to = 'exams_app_3/item')
    explanation = models.CharField(max_length = 1000, null = True)
    explanation_image = models.ImageField(blank = True, null = True)
    access_count = models.ManyToManyField(MCQAccessCount)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['?']

class Exam(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)
    items = models.ManyToManyField(MCQ)

    def __str__(self):
        return self.title

class ExamTicket(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE)
    date_start = models.DateTimeField(null = True)
    date_finish = models.DateTimeField(null = True)
    score = models.PositiveSmallIntegerField(null = True, blank = True)
    answers = models.ManyToManyField(Choice)
    items = models.PositiveSmallIntegerField(null = True, blank = True)
    percentage = models.FloatField(null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, related_name = 'user3')

    def __str__(self):
        return f"""{self.exam.title}: {self.user.last_name}, {self.user.first_name} : {self.date_start}, {self.date_finish}, {self.percentage}"""

    def get_absolute_url(self):
        return reverse('exams_app_3:exam_result', kwargs = {'pk':self.pk})
