from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Item)
admin.site.register(models.AnswerSheet)
admin.site.register(models.AnswerKey)
admin.site.register(models.ExamFile)
admin.site.register(models.Exam)
