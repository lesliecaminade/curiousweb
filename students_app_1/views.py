from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                DeleteView, CreateView,
                                UpdateView)
from . import models
from . import forms
from . import emailing
from main_app.models import User

from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password

import requests
import random
import string

class StudentSuccessEnrollment(TemplateView):
    template_name = 'students_app_1/enrollment_success.html'

class StudentFailEnrollment(TemplateView):
    template_name = 'students_app_1/enrollment_fail.html'

class StudentListViewAll(PermissionRequiredMixin, ListView):
    permission_required = ('students_app_1.view_student')
    model = models.Student

class StudentListViewEnrolled(PermissionRequiredMixin, ListView):
    permission_required = ('students_app_1.view_student')
    model = models.Student
    def get_queryset(self):
        return models.Student.objects.filter(enrolled = True)

class StudentListViewNotEnrolled(PermissionRequiredMixin, ListView):
    permission_required = ('students_app_1.view_student')
    model = models.Student
    def get_queryset(self):
        return models.Student.objects.filter(enrolled = False)

class StudentDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('students_app_1.view_student')
    context_object_name = 'student_details'
    model = models.Student

class StudentCreateView(CreateView):
    model = models.Student
    form_class = forms.StudentForm
    success_url = reverse_lazy('students_app_1:success')

    def form_valid(self, form):
        self.object = form.save(commit=False)

        recaptcha_response = self.request.POST['g-recaptcha-response'] #get google recapthcha response from form
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = {
            'secret':'6Lc1CO4UAAAAACs9XqPf35SGvdtP-0QmDM0n0K6V',
            'response': recaptcha_response,
        })
        r = r.json()
        if r['success'] == 'false':
            return HttpResponseRedirect(reverse('students_app_1:fail'))

        #then we create a user account for the student
        temp_password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        new_user = User.objects.create(
            first_name = self.request.POST['first_name'],
            last_name = self.request.POST['last_name'],
            username = (self.request.POST['first_name'].lower() + self.request.POST['last_name'].lower() + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))).replace(' ',''),
            password = make_password(temp_password),
            email = self.request.POST['email'],
            is_student = True,
            is_ece = True,
        )

        self.object.user = new_user
        self.object.save()

        try:
            emailing.send_email(self.object, temp_password) #send an email with enrollment details
        except:
            pass

        return super().form_valid(form)

class StudentUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('students_app_1.change_student')
    template_name = 'students_app_1/student_update.html'
    fields = '__all__'
    model = models.Student
    success_url = reverse_lazy("students_app_1:list_all")

class StudentDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('students_app_1.delete_student')
    permission_required = ('is_staff')
    model = models.Student
    success_url = reverse_lazy("students_app_1:list_all")
