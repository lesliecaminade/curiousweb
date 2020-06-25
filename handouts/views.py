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
from datetime import datetime


class Handouts(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                handouts = models.Handout.objects.all().order_by('-pk')
            elif self.request.user.is_ece:
                handouts = models.Handout.objects.filter(is_ece = True).order_by('-pk')
            elif self.request.user.is_ee:
                handouts = models.Handout.objects.filter(is_ee = True).order_by('-pk')
            elif self.request.user.is_tutorial:
                handouts = models.Handout.objects.filter(is_tutorial = True).order_by('-pk')
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
                'number_of_files': [i for i in range(10)],
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
                timestamp = datetime.now(),
            )
            new_handout.save()
            resize_image_field(new_handout.image, height = 300)

            for i in range(10):
                if self.request.FILES.get('handout_file_' + str(i)):
                    new_handoutfile = models.HandoutFile(
                        name = self.request.POST.get('name'),
                        file = self.request.FILES.get('handout_file_' + str(i)),
                        is_ece = is_ece,
                        is_ee = is_ee,
                        is_tutorial = is_tutorial,
                        is_accessible = is_accessible,
                    )
                    new_handoutfile.save()
                    new_handout.files.add(new_handoutfile)

            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'handouts',}))

class DownloadHandoutFile(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            handoutfile = models.HandoutFile.objects.get(pk = int(self.kwargs['filepk']))
            if  handoutfile.is_accessible:
                filename = handoutfile.file.name.split('/')[-1]
                response = HttpResponse(handoutfile.file, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename=%s' % filename
                return response
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
            file = self.request.FILES['file'],
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
        if self.request.user.is_superuser:
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
            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'handouts'}))
        else:
            return HttpResponse('Not allowed.')

class HandoutLock(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            handout = models.Handout.objects.filter(pk = int(self.kwargs.get('handoutpk'))).update(is_accessible=False)
            handout = models.Handout.objects.get(pk = int(self.kwargs.get('handoutpk')))
            for file in handout.files.all():
                file.is_accessible = False
                file.save()
            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'handouts'}))

class HandoutUnlock(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            handout = models.Handout.objects.filter(pk = int(self.kwargs.get('handoutpk'))).update(is_accessible=True)
            handout = models.Handout.objects.get(pk = int(self.kwargs.get('handoutpk')))
            for file in handout.files.all():
                file.is_accessible = True
                file.save()
            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'handouts'}))

class ToggleFlag(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            handout = models.Handout.objects.filter(pk = int(self.kwargs.get('pk')))
            flag = self.kwargs.get('flag')
            if self.kwargs.get('flag') == 'is_ece':
                handout.update(is_ece = not handout[0].is_ece)
            elif self.kwargs.get('flag') == 'is_ee':
                handout.update(is_ee = not handout[0].is_ee)
            elif self.kwargs.get('flag') == 'is_tutorial':
                handout.update(is_tutorial = not handout[0].is_tutorial)

            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'handouts'}))
