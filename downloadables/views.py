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
from .image_helpers import Thumbnail
from communications.standard_email import send_email
from datetime import datetime

class Downloadables(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                downloadables = models.Downloadable.objects.all().order_by('-pk')
            elif self.request.user.is_ece:
                downloadables = models.Downloadable.objects.filter(is_ece = True).order_by('-pk')
            elif self.request.user.is_ee:
                downloadables = models.Downloadable.objects.filter(is_ee = True).order_by('-pk')
            elif self.request.user.is_tutorial:
                downloadables = models.Downloadable.objects.filter(is_tutorial = True).order_by('-pk')
            else:
                send_email(ADMIN_EMAILS, 'ERROR REPORT',
                """Site: certconlinereview
                App: downloadables
                View: Downloadables"""
                )

            context = {
                'downloadables': downloadables,
            }

            template_name = 'downloadables/main.html'
            return render(self.request, template_name, context)

class AddDownloadable(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            template_name = 'downloadables/add.html'
            context = {
                'form': forms.DownloadableForm,
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

            new_downloadable = models.Downloadable(
                name = self.request.POST.get('name'),
                description = self.request.POST.get('description'),
                image = image_file,
                is_ece = is_ece,
                is_ee = is_ee,
                is_tutorial = is_tutorial,
                is_accessible = is_accessible,
                timestamp = datetime.now(),
            )
            new_downloadable.save()

            image_generator = Thumbnail(source=new_downloadable.image)
            modified_image_file = image_generator.generate()
            dest = open(new_downloadable.image.path, 'wb')
            dest.write(modified_image_file.read())
            dest.close()

            for i in range(10):
                if self.request.FILES.get('downloadable_file_' + str(i)):
                    new_downloadablefile = models.DownloadableFile(
                        name = self.request.POST.get('name'),
                        file = self.request.FILES.get('downloadable_file_' + str(i)),
                        is_ece = is_ece,
                        is_ee = is_ee,
                        is_tutorial = is_tutorial,
                        is_accessible = is_accessible,
                    )
                    new_downloadablefile.save()
                    new_downloadable.files.add(new_downloadablefile)

            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'downloadables',}))

class DownloadDownloadableFile(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            downloadablefile = models.DownloadableFile.objects.get(pk = int(self.kwargs['filepk']))
            if  downloadablefile.is_accessible:
                filename = downloadablefile.file.name.split('/')[-1]
                response = HttpResponse(downloadablefile.file, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename=%s' % filename
                return response
            else:
                return HttpResponse('Sorry, download not accessible.')

class AddDownloadableFile(View):
    def get(self, *args, **kwargs):
        downloadablepk = int(self.kwargs['downloadablepk'])
        form = forms.DownloadableFileForm
        template_name = 'downloadables/addfile.html'
        context = {
            'form': form,
            'downloadablepk': downloadablepk,
        }
        return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        downloadablepk = int(self.request.POST.get('downloadablepk'))
        downloadable = models.Downloadable.objects.get(pk = downloadablepk)

        new_downloadablefile = models.DownloadableFile(
            name = self.request.POST.get('name'),
            file = self.request.FILES['file'],
            is_ece = downloadable.is_ece,
            is_ee = downloadable.is_ee,
            is_tutorial = downloadable.is_tutorial,
            is_accessible = downloadable.is_accessible,
        )
        new_downloadablefile.save()


        downloadable.files.add(new_downloadablefile)

        return HttpResponseRedirect(reverse('downloadables:detail', kwargs = {'downloadablepk': downloadablepk, }))

class DownloadableDetail(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            downloadablepk = int(self.kwargs['downloadablepk'])
            downloadable = models.Downloadable.objects.get(pk = downloadablepk)
            template_name = 'downloadables/downloadable_view.html'
            context = {
                'downloadable': downloadable,
            }
            return render(self.request, template_name, context)

class DownloadableDelete(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            downloadablepk = int(self.kwargs['downloadablepk'])
            downloadable = models.Downloadable.objects.get(pk = downloadablepk)
            downloadable.delete()
            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'downloadables'}))
        else:
            return HttpResponse('Not allowed.')

class DownloadableLock(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            downloadable = models.Downloadable.objects.filter(pk = int(self.kwargs.get('downloadablepk'))).update(is_accessible=False)
            downloadable = models.Downloadable.objects.get(pk = int(self.kwargs.get('downloadablepk')))
            for file in downloadable.files.all():
                file.is_accessible = False
                file.save()
            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'downloadables'}))

class DownloadableUnlock(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            downloadable = models.Downloadable.objects.filter(pk = int(self.kwargs.get('downloadablepk'))).update(is_accessible=True)
            downloadable = models.Downloadable.objects.get(pk = int(self.kwargs.get('downloadablepk')))
            for file in downloadable.files.all():
                file.is_accessible = True
                file.save()
            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'downloadables'}))

class ToggleFlag(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            downloadable = models.Downloadable.objects.filter(pk = int(self.kwargs.get('pk')))
            flag = self.kwargs.get('flag')
            if self.kwargs.get('flag') == 'is_ece':
                downloadable.update(is_ece = not downloadable[0].is_ece)
            elif self.kwargs.get('flag') == 'is_ee':
                downloadable.update(is_ee = not downloadable[0].is_ee)
            elif self.kwargs.get('flag') == 'is_tutorial':
                downloadable.update(is_tutorial = not downloadable[0].is_tutorial)

            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'downloadables'}))
