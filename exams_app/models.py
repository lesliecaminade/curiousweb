from django.db import models
from main_app.models import User
from django.urls import reverse_lazy, reverse

class MCQ(models.Model):
    question = models.TextField(max_length = 1000)
    choice1 = models.TextField(max_length = 500, default = '')
    choice2 = models.TextField(max_length = 500, default = '')
    choice3 = models.TextField(max_length = 500, default = '')
    choice4 = models.TextField(max_length = 500, default = '')
    correct1 = models.BooleanField(default = False)
    correct2 = models.BooleanField(default = False)
    correct3 = models.BooleanField(default = False)
    correct4 = models.BooleanField(default = False)
    explanation = models.TextField(max_length = 1000)

    def get_absolute_url(self):
        return reverse("exams_app:mcq_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.question

class Exam(models.Model):
    author = models.ForeignKey(User, on_delete = models.PROTECT)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    is_premium = models.BooleanField()
    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)
    items = models.ManyToManyField(MCQ)

    def __str__(self):
        return self.title

class CategoryA(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    exams = models.ManyToManyField(Exam)

    def __str__(self):
        return self.name

class CategoryB(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    categoryas = models.ManyToManyField(CategoryA)

    def __str__(self):
        return self.name
