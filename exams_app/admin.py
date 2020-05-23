from django.contrib import admin
from .models import Choice, MCQ, Exam, CategoryA, CategoryB, ExamTicket


admin.site.register(Choice)
admin.site.register(MCQ)
admin.site.register(Exam)
admin.site.register(CategoryA)
admin.site.register(CategoryB)
admin.site.register(ExamTicket)
