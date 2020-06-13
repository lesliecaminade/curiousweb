from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                DeleteView, CreateView,
                                UpdateView)
from . import models
from .image_helpers import resize_image_field

RESIZE_HEIGHT = 300
# Create your views here.
class Testimonial(View):
    def get(self, *args, **kwargs):
        testimonies = models.Testimony.objects.all().order_by('?')
        template_name = 'testimonials/testimonial_list.html'
        context = {
            'testimonies': testimonies,
        }
        return render(self.request, template_name, context)

class CreateTestimony(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            template_name = 'testimonials/testimonial_form.html'
            context = {
                'mode': 'Create',
            }
            return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        if self.request.user.is_superuser:
            new_testimony = models.Testimony(
                name = self.request.POST.get('name'),
                testimony = self.request.POST.get('testimony'),
                thumbnail = self.request.FILES.get('thumbnail'),
            )
            new_testimony.save()
            resize_image_field(new_testimony.thumbnail, height = 300)
            return HttpResponseRedirect(reverse('testimonials:all'))

class DeleteTestimony(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            testimony = models.Testimony.objects.get(pk  = int(self.kwargs.get('pk')))
            testimony.delete()
            return HttpResponseRedirect(reverse('testimonials:all'))

class EditTestimony(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            template_name = 'testimonials/testimonial_form.html'
            testimony = models.Testimony.objects.get(pk = int(self.kwargs.get('pk')))
            context = {
                'mode': 'Create',
                'testimony': testimony,
                'pk': testimony.pk,
            }
            return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        if self.request.user.is_superuser:
            if self.request.FILES.get('thumbnail'):
                testimony = models.Testimony.objects.filter(pk = int(self.request.POST.get('pk'))).update(
                    name = self.request.POST.get('name'),
                    testimony = self.request.POST.get('testimony'),
                    thumbnail = self.request.FILES.get('thumbnail'),
                )
                resize_image_field(testimony.thumbnail, height = RESIZE_HEIGHT)
            else:
                testimony = models.Testimony.objects.filter(pk = int(self.request.POST.get('pk'))).update(
                    name = self.request.POST.get('name'),
                    testimony = self.request.POST.get('testimony'),
                )
            return HttpResponseRedirect(reverse('testimonials:all'))

class ShowTestimony(View):
    def get(self, *args, **kwargs):
        testimony = models.Testimony.objects.get(pk = int(self.kwargs.get('pk')))
        template_name = 'testimonials/testimonial_detail.html'
        context = {
            'testimony': testimony,
        }
        return render(self.request, template_name, context)
