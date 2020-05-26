from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                DeleteView, CreateView,
                                UpdateView)
from django.views.static import serve
import os

from . import models
from . import forms
from PIL import Image
from .image_helpers import resize_image_field

class Handouts(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                handouts = models.Handout.objects.all()
            elif self.request.user.is_ece:
                handouts = models.Handout.objects.filter(is_ece = True)
            elif self.request.user.is_ee:
                handouts = models.Handout.objects.filter(is_ee = True)
            elif self.request.user.is_tutorial:
                handouts = models.Handout.objects.filter(is_tutorial = True)
            else:
                pass



            context = {
                'handouts': handouts,
            }

            template_name = 'handouts/main.html'
            return render(self.request, template_name, context)

class AddHandout(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            template_name = 'handouts/add.html'
            context = {
                'form': forms.HandoutForm,
            }
            return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        if self.request.user.is_superuser:
            try:
                file = self.request.FILES['file']
            except:
                file = None

            try:
                image_file = self.request.FILES['image']
            except:
                image_file = None

            if self.request.POST.get('is_ece'):
                is_ece = True
            else:
                is_ece = False

            if self.request.POST.get('is_ee'):
                is_ee = True
            else:
                is_ee = False

            if self.request.POST.get('is_tutorial'):
                is_tutorial = True
            else:
                is_tutorial = False

            if self.request.POST.get('is_accessible'):
                is_accessible = True
            else:
                is_accessible = False

            new_handout = models.Handout(
                name = self.request.POST.get('name'),
                description = self.request.POST.get('description'),
                file = file,
                image = image_file,
                is_ece = is_ece,
                is_ee = is_ee,
                is_tutorial = is_tutorial,
                is_accessible = is_accessible,
            )
            new_handout.save()
            resize_image_field(new_handout.image, height = 300)

            return HttpResponseRedirect(reverse('handouts:main'))

class DownloadHandout(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            handout = models.Handout.objects.get(pk = int(self.kwargs['handout']))
            filepath = handout.file.path
            return serve(self.request, os.path.basename(filepath), os.path.dirname(filepath))
