from django.contrib import admin
from main_app.models import ErrorReport
from main_app.models import Topic, Subtopic, MultipleChoice, Student
# Register your models here.


admin.site.register(ErrorReport)
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(MultipleChoice)
admin.site.register(Student)
