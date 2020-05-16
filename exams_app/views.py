from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                DeleteView, CreateView,
                                UpdateView)
from . import models
from . import forms

from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.shortcuts import get_object_or_404


# Create your views here.
class ExamTemplateView(TemplateView):
    template_name = 'exams_app/exam_management.html'

class CategoryListView(ListView):
    model = models.Category

class CategoryCreateView(CreateView):
    model = models.Category
    fields = '__all__'
    success_url = reverse_lazy('exams_app:category_list')

class CategoryDetailView(DetailView):
    model = models.Category
    fields = '__all__'
    context_object_name = 'category_details'

class CategoryUpdateView(UpdateView):
    fields = '__all__'
    model = models.Category
    success_url = reverse_lazy('exams_app:category_list')

class CategoryDeleteView(DeleteView):
    model = models.Category
    success_url = reverse_lazy('exams_app:category_list')



class SubcategoryListView(ListView):
    model = models.Subcategory

class SubcategoryCreateView(CreateView):
    model = models.Subcategory
    fields = '__all__'
    success_url = reverse_lazy('exams_app:subcategory_list')

class SubcategoryDetailView(DetailView):
    model = models.Subcategory
    fields = '__all__'
    context_object_name = 'subcategory_details'

class SubcategoryUpdateView(UpdateView):
    fields = '__all__'
    model = models.Subcategory
    success_url = reverse_lazy('exams_app:subcategory_list')

class SubcategoryDeleteView(DeleteView):
    model = models.Subcategory
    success_url = reverse_lazy('exams_app:subcategory_list')




class SubsubcategoryListView(ListView):
    model = models.Subsubcategory

class SubsubcategoryCreateView(CreateView):
    model = models.Subsubcategory
    fields = '__all__'
    success_url = reverse_lazy('exams_app:subsubcategory_list')

class SubsubcategoryDetailView(DetailView):
    model = models.Subsubcategory
    fields = '__all__'
    context_object_name = 'subsubcategory_details'

class SubsubcategoryUpdateView(UpdateView):
    fields = '__all__'
    model = models.Subsubcategory
    success_url = reverse_lazy('exams_app:subsubcategory_list')

class SubsubcategoryDeleteView(DeleteView):
    model = models.Subsubcategory
    success_url = reverse_lazy('exams_app:subsubcategory_list')

class ExamListView(ListView):
    model = models.Exam

class ExamStudentListView(ListView):
    model = models.Exam
    template_name = 'exams_app/exam_list_student.html'

class ExamCreateView(CreateView):
    model = models.Exam
    fields = '__all__'
    success_url = reverse_lazy('exams_app:exam_list')

class ExamDetailView(DetailView):
    model = models.Exam
    fields = '__all__'
    context_object_name = 'exam_details'

class ExamUpdateView(UpdateView):
    fields = '__all__'
    model = models.Exam
    success_url = reverse_lazy('exams_app:exam_list')

class ExamDeleteView(DeleteView):
    model = models.Exam
    success_url = reverse_lazy('exams_app:exam_list')


class McqListView(ListView):
    model = models.MCQuestion

class McqCreateView(CreateView):
    model = models.MCQuestion
    fields = '__all__'
    success_url = reverse_lazy('exams_app:mcq_list')

class McqDetailView(DetailView):
    model = models.MCQuestion
    fields = '__all__'
    context_object_name = 'mcquestion_details'

class McqUpdateView(UpdateView):
    fields = '__all__'
    model = models.MCQuestion
    success_url = reverse_lazy('exams_app:mcq_list')

class McqDeleteView(DeleteView):
    model = models.MCQuestion
    success_url = reverse_lazy('exams_app:mcq_list')
