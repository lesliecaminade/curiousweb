from django.contrib import admin
from main_app.models import ErrorReport
from main_app.models import (
Topic,
Subtopic,
Subsubtopic,
 MultipleChoice,
 Student,
 ElectronicsStudent,
 ElectricalStudent,
 TutorialStudent,)
# Register your models here.

admin.site.register(ErrorReport)
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(Subsubtopic)
admin.site.register(MultipleChoice)
admin.site.register(Student)
admin.site.register(ElectricalStudent)
admin.site.register(ElectronicsStudent)
admin.site.register(TutorialStudent)
