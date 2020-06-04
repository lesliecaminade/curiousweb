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
import handouts
import exams_app
import exams_app_2
import communications
import curiousweb
from datetime import datetime

# Create your views here.
class IndexView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                template_name = 'main_app/dashboard_admin.html'
                announcements = models.Announcement.objects.all()[:5]
                enrolls = models.User.objects.all().order_by('-date_created')[:5]
                exams = exams_app_2.models.Exam.objects.all().order_by('-pk')[:5]
                hand = handouts.models.Handout.objects.all().order_by('-pk')[:5]
                context = {
                    'nav_home': 'active',
                    'announcements': announcements,
                    'exams': exams,
                    'handouts': hand,
                    'enrollments': enrolls,
                    #activities
                    }
                return render(self.request, template_name, context)
            else:
                if self.request.user.is_ece:
                    announcements = models.Announcement.objects.filter(is_ece = True)[:5]
                    exams = exams_app_2.models.Exam.objects.filter(is_ece = True).order_by('-pk')[:5]
                    hand = handouts.models.Handout.objects.filter(is_ece = True).order_by('-pk')[:5]
                elif self.request.user.is_ee:
                    announcements = models.Announcement.objects.filter(is_ee = True)[:5]
                    exams = exams_app_2.models.Exam.objects.filter(is_ee = True).order_by('-pk')[:5]
                    hand = handouts.models.Handout.objects.filter(is_ee = True).order_by('-pk')[:5]
                elif self.request.user.is_tutorial:
                    announcements = models.Announcement.objects.filter(is_tutorial = True)[:5]
                    exams = exams_app_2.models.Exam.objects.filter(is_tutorial = True).order_by('-pk')[:5]
                    hand = handouts.models.Handout.objects.filter(is_tutorial = True).order_by('-pk')[:5]
                else:
                    HttpResponse('unhandled user type')

                template_name = 'main_app/dashboard_student.html'
                context = {
                    'nav_home': 'active',
                    'announcements': announcements,
                    'exams': exams,
                    'handouts': hand,
                    }
                return render(self.request, template_name, context)
        else:
            template_name = 'main_app/index.html'
            context = {
                'nav_home': 'active',
                }
            return render(self.request, template_name, context)


class EnrollView(TemplateView):
    template_name = 'main_app/enroll.html'
    extra_context = {
        'nav_enroll': 'active',
    }

class LogoutView(TemplateView):
    template_name = 'main_app/logout_success.html'

class UserListView(View):
    def get(self, *args, **kwargs):
        users = models.User.objects.all().order_by('-pk')
        context = {
            'users': users,
            'nav_admin': 'active',
            'active_filter': 'all',
        }
        template_name = 'main_app/users_list.html'
        if self.request.user.is_superuser:
            return render(self.request, template_name, context)
        else:
            return HttpResponseRedirect(reverse('login'))

class UserListFilterView(View):
    def get(self, *args, **kwargs):
        try:
            filter = self.kwargs.get('filter')
            if filter.lower() == 'ece':
                users = models.User.objects.filter(is_ece = True).order_by('-pk')
            elif filter.lower() == 'ee':
                users = models.User.objects.filter(is_ee = True).order_by('-pk')
            elif filter.lower() == 'tutorial':
                users = models.User.objects.filter(is_tutorial = True).order_by('-pk')
            elif filter.lower() == 'active':
                users = models.User.objects.filter(is_active = True).order_by('-pk')
            elif filter.lower() == 'inactive':
                users = models.User.objects.filter(is_active = False).order_by('-pk')
            elif filter.lower() == 'all':
                users = models.User.objects.all().order_by('-pk')
            else:
                communications.standard_email.send_email(curiousweb.settings.ADMIN_EMAILS, 'certconlinereview ERROR', 'unhandled user type in main_app.views UserListFilterView class')

            context = {
                'users': users,
                'nav_admin': 'active',
                'active_filter': filter,
            }
            template_name = 'main_app/users_list.html'
            if self.request.user.is_superuser:
                return render(self.request, template_name, context)
            else:
                return HttpResponseRedirect(reverse('login'))
        except:
            communications.standard_email.send_email(curiousweb.settings.ADMIN_EMAILS, 'certconlinereview ERROR', 'error in main_app.views.UserListFilterView')

class UserView(View):
    def get(self, *args, **kwargs):
        user = models.User.objects.get(pk = self.kwargs['pk'])
        tickets = exams_app.models.ExamTicket.objects.filter(user = user)
        answer_sheets = exams_app_2.models.AnswerSheet.objects.filter(user = user)
        context = {
            'user': user,
            'nav_admin': 'active',
            'tickets': tickets,
            'answer_sheets': answer_sheets,
        }
        template_name = 'main_app/user_detail.html'
        if self.request.user.is_superuser:
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


class DeactivateUser(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            user = models.User.objects.filter(pk = int(self.kwargs.get('userpk'))).update(is_active = False)
            return HttpResponseRedirect(reverse('main_app:users'))

class ActivateUser(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            user = models.User.objects.filter(pk = int(self.kwargs.get('userpk'))).update(is_active = True)
            return HttpResponseRedirect(reverse('main_app:users'))

class CreateAnnouncement(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            form = forms.AnnouncementForm
            template_name = 'main_app/create_announcement.html'
            context = {
                'form': form,
            }
            return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        if self.request.user.is_superuser:
            new_announcement = models.Announcement(
                title = self.request.POST.get('title'),
                type = self.request.POST.get('type'),
                content = self.request.POST.get('content'),
                timestamp = datetime.now(),
                is_ece = bool(self.request.POST.get('is_ece')),
                is_ee = bool(self.request.POST.get('is_ee')),
                is_tutorial = bool(self.request.POST.get('is_tutorial')),
                is_online_class = bool(self.request.POST.get('is_online_class')),
            )
            new_announcement.save()

            return HttpResponseRedirect(reverse('index'))

class DeleteAnnouncement(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            ann = models.Announcement.objects.get(pk = int(self.kwargs.get('announcementpk')))
            ann.delete()
            return HttpResponseRedirect(reverse('index'))
