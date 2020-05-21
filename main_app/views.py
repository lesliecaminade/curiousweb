from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
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
from django.contrib import messages

# Create your views here.
class IndexView(TemplateView):
    template_name = 'main_app/index.html'
    extra_context = {
        'nav_home': 'active',
    }

class EnrollView(TemplateView):
    template_name = 'main_app/enroll.html'
    extra_context = {
        'nav_enroll': 'active',
    }

class LogoutView(TemplateView):
    template_name = 'main_app/logout_success.html'

class UserListView(View):
    def get(self, *args, **kwargs):
        users = models.User.objects.all()
        context = {
            'users': users,
            'nav_admin': 'active',
        }
        template_name = 'main_app/users_list.html'
        if self.request.user.is_teacher:
            return render(self.request, template_name, context)
        else:
            return HttpResponseRedirect(reverse('login'))

class UserView(View):
    def get(self, *args, **kwargs):
        user = models.User.objects.get(pk = self.kwargs['pk'])
        context = {
            'user': user,
            'nav_admin': 'active',
        }
        template_name = 'main_app/user_detail.html'
        if self.request.user.is_teacher:
            return render(self.request, template_name, context)
        else:
            return HttpResponseRedirect(reverse('login'))

class ChangePasswordView(View):
    def get(self, *args, **kwargs):
        template = 'main_app/change_password.html'
        return render(self.request, template)

    def post(self, *args, **kwargs):
        password = self.request.POST.get('password')
        confirm_password = self.request.POST.get('confirm_password')
        if password == confirm_password:
            user = self.request.user
            user.set_password(password)
            user.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(self.request, 'main_app/basic_feedback', {
                'title': 'Passwords do not match',
                'description': 'Please press Back on you browser to try again.',
            } )
