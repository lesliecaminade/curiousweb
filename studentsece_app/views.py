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
class StudentECESuccessEnrollment(TemplateView):
    template_name = 'studentsece_app/enrollment_success.html'

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
        #self.object.user = self.request.user
        emailing.send_email(self.object)
        self.object.save()
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
