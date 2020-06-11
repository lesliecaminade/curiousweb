from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                DeleteView, CreateView,
                                UpdateView)



from . import models

class ScheduleECE(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            template_name = 'staticpages/schedule_ece.html'
            return render(self.request, template_name)

class ScheduleEE(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            template_name = 'staticpages/schedule_ee.html'
            return render(self.request, template_name)

class Location(View):
    def get(self, *args, **kwargs):
        template_name = 'staticpages/location.html'
        return render(self.request, template_name)

class Reviewers(View):
    def get(self, *args, **kwargs):
        template_name = 'staticpages/reviewers.html'
        return render(self.request, template_name)
        
