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
from main_app.models import User

from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.shortcuts import get_object_or_404

import requests
import random
import string
from django.contrib.auth.hashers import make_password

class StudentTutorialSuccessEnrollment(TemplateView):
    template_name = 'studentstutorial_app/enrollment_success.html'

class StudentTutorialFailEnrollment(TemplateView):
    template_name = 'studentstutorial_app/enrollment_fail.html'

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

        recaptcha_response = self.request.POST['g-recaptcha-response'] #get ggoogle recapthcha response from form
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = {
            'secret':'6Lc1CO4UAAAAACs9XqPf35SGvdtP-0QmDM0n0K6V',
            'response': recaptcha_response,
        })
        r = r.json()
        if r['success'] == 'false':
            return HttpResponseRedirect(reverse('studentstutorial_app:fail'))

        #then we create a user account for the student
        temp_password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        new_user = User.objects.create(
            first_name = self.request.POST['first_name'],
            last_name = self.request.POST['last_name'],
            username = self.request.POST['first_name'].lower() + self.request.POST['last_name'].lower(),
            password = make_password(temp_password),
            email = self.request.POST['email'],
            is_student = True,
            is_tutorial = True,
        )

        self.object.user = new_user
        self.object.save()

        try:
            emailing.send_email(self.object, temp_password) #send an email with enrollment details
        except:
            pass

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
