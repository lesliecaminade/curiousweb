from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                DeleteView, CreateView,
                                UpdateView)
from . import models
from . import forms
from . import emailing

from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.shortcuts import get_object_or_404
# Create your views here.

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')
#
#
class StudentTutorialSuccessEnrollment(TemplateView):
    template_name = 'studentstutorial_app/enrollment_success.html'

class StudentTutorialListViewAll(PermissionRequiredMixin, ListView):
    permission_required = ('studentstutorial_app.view_studenttutorial')
    model = models.StudentTutorial

class StudentTutorialListViewEnrolled(PermissionRequiredMixin, ListView):
    permission_required = ('studentstutorial_app.view_studenttutorial')
    model = models.StudentTutorial
    def get_queryset(self):
        return models.StudentTutorial.objects.filter(enrolled = True)

class StudentTutorialListViewNotEnrolled(PermissionRequiredMixin, ListView):
    permission_required = ('studentstutorial_app.view_studenttutorial')
    model = models.StudentTutorial
    def get_queryset(self):
        return models.StudentTutorial.objects.filter(enrolled = False)

class StudentTutorialDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('studentstutorial_app.view_studenttutorial')
    context_object_name = 'studenttutorial_details'
    model = models.StudentTutorial
    #template_name = 'students_app/student_detail.html'

class StudentTutorialCreateView(CreateView):
    model = models.StudentTutorial
    form_class = forms.StudentTutorialForm
    success_url = reverse_lazy('studentstutorial_app:success')

    def form_valid(self, form):
        ""
        self.object = form.save(commit=False)
        #self.object.user = self.request.user
        emailing.send_email(self.object)
        self.object.save()
        return super().form_valid(form)

class StudentTutorialUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('studentstutorial_app.change_studenttutorial')
    template_name = 'students_app/students_update.html'
    fields = '__all__'
    model = models.StudentTutorial
    success_url = reverse_lazy("studentstutorial_app:list_all")

class StudentTutorialDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('studentstutorial_app.delete_studenttutorial')
    permission_required = ('is_staff')
    model = models.StudentTutorial
    success_url = reverse_lazy("studentstutorial_app:list_all")
