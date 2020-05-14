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
# Create your views here.

# Original Function View:
#
# def index(request):
#     return render(request,'index.html')
#
#

# Pretty simple right?
class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)

        context['injectme'] = "Basic Injection!" #this is how to insert context data into the template
        return context

class StudentECESuccessEnrollment(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'studentsece_app/success.html'

class StudentECEListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    model = models.StudentECE

class StudentECEDetailView(DetailView):
    context_object_name = 'studentece_details'
    model = models.StudentECE
    template_name = 'studentsece_app/studentece_detail.html'

class StudentECECreateView(CreateView):
    model = models.StudentECE
    form_class = forms.StudentECEForm
    success_url = reverse_lazy('studentsece_app:success')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        #self.object.user = self.request.user

        emailing.send_email(self.object)

        self.object.save()
        return super().form_valid(form)


class StudentECEUpdateView(UpdateView):
    fields = [
        'first_name',
        'last_name',
        'middle_name',
        'birthdate',
        'address',
        'religion',
        'mobile_number',
    ]
    model = models.StudentECE

class StudentECEDeleteView(DeleteView):
    model = models.StudentECE
    success_url = reverse_lazy("studentsece_app:list")
