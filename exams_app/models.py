from django.db import models
from main_app.models import User
from django.urls import reverse_lazy, reverse

class Choice(models.Model):
    content = models.CharField(max_length = 1000)
    correct = models.BooleanField()
    image = models.ImageField(null = True, blank = True)
    explanation = models.CharField(max_length = 1000, null = True)

    def __str__(self):
        return content

class MCQ(models.Model):
    question = models.TextField(max_length = 1000, default = '', null = True, blank = True)
    choices = models.ManyToManyField(Choice)
    image = models.ImageField(blank = True, null = True)

    def get_absolute_url(self):
        return reverse("exams_app:mcq_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.question

class Exam(models.Model):
    author = models.ForeignKey(User, on_delete = models.PROTECT, null = True)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)
    items = models.ManyToManyField(MCQ)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('exams_app:exam', kwargs={'pk':self.pk})

class CategoryA(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100, blank = True, null = True)
    exams = models.ManyToManyField(Exam, blank = True)
    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('exams_app:categoryb', kwargs = {'pk': self.pk})
        return reverse('exams_app:exams_list', kwargs = {'pk': self.pk})

class CategoryB(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100, blank = True, null = True)
    categoryas = models.ManyToManyField(CategoryA, blank = True)
    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exams_app:categorya', kwargs = {'pk': self.pk})

class ExamTicket(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE)
    date_start = models.DateTimeField(null = True)
    date_finish = models.DateTimeField(null = True)
    score = models.PositiveSmallIntegerField(null = True, blank = True)
    answers = models.ManyToManyField(Choice)
    items = models.PositiveSmallIntegerField(null = True, blank = True)
    percentage = models.FloatField(null = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return f"""{self.exam.title}: {self.user.last_name}, {self.user.first_name} : {self.date_start}, {self.date_finish}, {self.percentage}"""

    def get_absolute_url(self):
        return reverse('exams_app:exam_result', kwargs = {'pk':self.pk})
