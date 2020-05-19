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
# Create your views here.

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')
#
#
class StudentECESuccessEnrollment(TemplateView):
    template_name = 'studentsece_app/enrollment_success.html'

class StudentECEFailEnrollment(TemplateView):
    template_name = 'studentsece_app/enrollment_fail.html'

class StudentECEListViewAll(PermissionRequiredMixin, ListView):
    permission_required = ('studentsece_app.view_studentece')
    model = models.StudentECE

class StudentECEListViewEnrolled(PermissionRequiredMixin, ListView):
    permission_required = ('studentsece_app.view_studentece')
    model = models.StudentECE
    def get_queryset(self):
        return models.StudentECE.objects.filter(enrolled = True)

class StudentECEListViewNotEnrolled(PermissionRequiredMixin, ListView):
    permission_required = ('studentsece_app.view_studentece')
    model = models.StudentECE
    def get_queryset(self):
        return models.StudentECE.objects.filter(enrolled = False)

class StudentECEDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('studentsece_app.view_studentece')
    context_object_name = 'studentece_details'
    model = models.StudentECE
    #template_name = 'studentsece_app/studentece_detail.html'

class StudentECECreateView(CreateView):
    model = models.StudentECE
    form_class = forms.StudentECEForm
    success_url = reverse_lazy('studentsece_app:success')

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
            return HttpResponseRedirect(reverse('studentsece_app:fail'))

        #then we create a user account for the student
        temp_password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
        new_user = User.objects.create(
            first_name = self.request.POST['first_name'],
            last_name = self.request.POST['last_name'],
            username = self.request.POST['first_name'].lower() + self.request.POST['last_name'].lower() + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3)),
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

class StudentECEUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('studentsece_app.change_studentece')
    template_name = 'studentsece_app/studentsece_update.html'
    fields = '__all__'
    model = models.StudentECE
    success_url = reverse_lazy("studentsece_app:list_all")

class StudentECEDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('studentsece_app.delete_studentece')
    permission_required = ('is_staff')
    model = models.StudentECE
    success_url = reverse_lazy("studentsece_app:list_all")
