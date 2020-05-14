from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                DeleteView, CreateView,
                                UpdateView)

from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from . import models
from . import forms

# Create your views here.
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'main_app/index.html'

class EnrollView(TemplateView):
    template_name = 'main_app/enroll.html'

class LogoutView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'main_app/logout_success.html'

# Create your views here.
class RegisterView(PermissionRequiredMixin,CreateView):
    permission_required = 'auth.add_user'
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("index")
    template_name = "main_app/register.html"

    def get_permission_denied_message(self):
        """
        Override this method to override the permission_denied_message attribute.
        """
        self.permission_denied_message = 'Only certain accounts can register new accounts. You are not allowed.'
        return self.permission_denied_message
