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
from communications.standard_email import send_email


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
                send_email(ADMIN_EMAILS, 'ERROR REPORT',
                """Site: certconlinereview
                App: handouts
                View: Handouts"""
                )

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
                image = image_file,
                is_ece = is_ece,
                is_ee = is_ee,
                is_tutorial = is_tutorial,
                is_accessible = is_accessible,
            )
            new_handout.save()
            resize_image_field(new_handout.image, height = 300)

            return HttpResponseRedirect(reverse('handouts:detail', kwargs = {'handoutpk': new_handout.pk,}))

class DownloadHandoutFile(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            handoutfile = models.HandoutFile.objects.get(pk = int(self.kwargs['filepk']))
            if handoutfile.is_accessible and ((self.request.user.is_ece and handoutfile.is_ece) or (self.request.user.is_ee and handoutfile.is_ee) or (self.request.user.is_tutorial and handoutfile.is_tutorial)) :
                filepath = handoutfile.file.path
                return serve(self.request, os.path.basename(filepath), os.path.dirname(filepath))
            else:
                return HttpResponse('Sorry, download not accessible.')

class AddHandoutFile(View):
    def get(self, *args, **kwargs):
        handoutpk = int(self.kwargs['handoutpk'])
        form = forms.HandoutFileForm
        template_name = 'handouts/addfile.html'
        context = {
            'form': form,
            'handoutpk': handoutpk,
        }
        return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        handoutpk = int(self.request.POST.get('handoutpk'))
        handout = models.Handout.objects.get(pk = handoutpk)

        new_handoutfile = models.HandoutFile(
            name = self.request.POST.get('name'),
            file = self.request.POST.get('file'),
            is_ece = handout.is_ece,
            is_ee = handout.is_ee,
            is_tutorial = handout.is_tutorial,
            is_accessible = handout.is_accessible,
        )
        new_handoutfile.save()


        handout.files.add(new_handoutfile)

        return HttpResponseRedirect(reverse('handouts:detail', kwargs = {'handoutpk': handoutpk, }))

class HandoutDetail(View):
    def get(self, *args, **kwargs):
        handoutpk = int(self.kwargs['handoutpk'])
        handout = models.Handout.objects.get(pk = handoutpk)
        template_name = 'handouts/handout_view.html'
        context = {
            'handout': handout,
        }
        return render(self.request, template_name, context)

class HandoutDelete(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            handoutpk = int(self.kwargs['handoutpk'])
            handout = models.Handout.objects.get(pk = handoutpk)
            handout.delete()
            return HttpResponseRedirect(reverse('handouts:main'))
        else:
            return HttpResponse('Not allowed.')
