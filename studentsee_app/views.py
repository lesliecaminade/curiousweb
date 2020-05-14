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
class StudentEESuccessEnrollment(TemplateView):
    template_name = 'studentsee_app/enrollment_success.html'

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
        #self.object.user = self.request.user
        emailing.send_email(self.object)
        self.object.save()
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
