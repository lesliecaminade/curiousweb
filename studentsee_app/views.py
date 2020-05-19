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
# Create your views here.

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')
#
#
class StudentEESuccessEnrollment(TemplateView):
    template_name = 'studentsee_app/enrollment_success.html'

class StudentEEFailEnrollment(TemplateView):
    template_name = 'studentsee_app/enrollment_fail.html'

class StudentEEListViewAll(PermissionRequiredMixin, ListView):
    permission_required = ('studentsee_app.view_studentee')
    model = models.StudentEE

class StudentEEListViewEnrolled(PermissionRequiredMixin, ListView):
    permission_required = ('studentsee_app.view_studentee')
    model = models.StudentEE
    def get_queryset(self):
        return models.StudentEE.objects.filter(enrolled = True)

class StudentEEListViewNotEnrolled(PermissionRequiredMixin, ListView):
    permission_required = ('studentsee_app.view_studentee')
    model = models.StudentEE
    def get_queryset(self):
        return models.StudentEE.objects.filter(enrolled = False)

class StudentEEDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('studentsee_app.view_studentee')
    context_object_name = 'studentee_details'
    model = models.StudentEE
    #template_name = 'studentsEE_app/studentEE_detail.html'

class StudentEECreateView(CreateView):
    model = models.StudentEE
    form_class = forms.StudentEEForm
    success_url = reverse_lazy('studentsee_app:success')

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
            return HttpResponseRedirect(reverse('studentsee_app:fail'))

        #then we create a user account for the student
        temp_password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        new_user = User.objects.create(
            first_name = self.request.POST['first_name'],
            last_name = self.request.POST['last_name'],
            username = self.request.POST['first_name'].lower() + self.request.POST['last_name'].lower() + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)),
            password = make_password(temp_password),
            email = self.request.POST['email'],
            is_student = True,
            is_ee = True,
        )

        self.object.user = new_user
        self.object.save()

        try:
            emailing.send_email(self.object, temp_password) #send an email with enrollment details
        except:
            pass

        return super().form_valid(form)

class StudentEEUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('studentsee_app.change_studentee')
    template_name = 'studentsee_app/studentsee_update.html'
    fields = '__all__'
    model = models.StudentEE
    success_url = reverse_lazy("studentsee_app:list_all")

class StudentEEDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('studentsee_app.delete_studentee')
    permission_required = ('is_staff')
    model = models.StudentEE
    success_url = reverse_lazy("studentsee_app:list_all")
