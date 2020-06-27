from django.db import models
from main_app.models import User
# Create your models here.


class Item(models.Model):
    item_number = models.PositiveSmallIntegerField()
    answer = models.CharField(max_length = 5)
    bonus = models.BooleanField(default = False)
    skip = models.BooleanField(default = False)

    def __str__(self):
        return str(self.item_number) + ' ' + self.answer

    class Meta:
        ordering = ['item_number']

class AnswerSheet(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    items = models.ManyToManyField(Item)
    score = models.PositiveSmallIntegerField(null = True, blank = True)
    percentage = models.FloatField(null = True, blank = True)
    date_submitted = models.DateField(null = True, blank = True)
    first_take = models.BooleanField(default = False)

    def __str__(self):
        return self.user_first_name +','+ self.user.last_name + ',' + str(self.score) + '% ' + str(self.date_submitted)

    class Meta:
        ordering = ['-score']

class AnswerKey(models.Model):
    items = models.ManyToManyField(Item)

class ExamFile(models.Model):
    name = models.CharField(max_length = 50, blank = True)
    file = models.FileField(upload_to = 'exams_app_2/examfiles')

    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)

class Exam(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100, blank = True)
    is_ece = models.BooleanField(default = False)
    is_ee = models.BooleanField(default = False)
    is_tutorial = models.BooleanField(default = False)
    is_accessible = models.BooleanField(default = False)
    files = models.ManyToManyField(ExamFile)
    answer_key = models.ForeignKey(AnswerKey, on_delete = models.CASCADE, null = True)
    answer_sheets = models.ManyToManyField(AnswerSheet)
    thumbnail = models.ImageField(upload_to = 'exams_app_2/thumbnails')
    is_done = models.BooleanField(default = False)
    timestamp = models.DateTimeField(null=True)


    def __str__(self):
        return self.name
