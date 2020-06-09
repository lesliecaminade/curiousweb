from django.contrib import admin
from . import models

admin.site.register(models.Choice)
admin.site.register(models.MCQ)
admin.site.register(models.Exam)
admin.site.register(models.ExamTicket)
