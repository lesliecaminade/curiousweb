from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, Http404
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                DeleteView, CreateView,
                                UpdateView)
from . import models
from . import forms

from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.timezone import make_aware
from openpyxl import Workbook
from openpyxl import load_workbook

class ExamCategoryBCreate(CreateView):
    template_name = 'exams_app/category_form.html'
    model = models.CategoryB
    fields = '__all__'
    success_url = reverse_lazy('exams_app:exams')
    extra_context = {
        'nav_exams': 'active',
    }

class ExamCategoryACreate(View):
    def get(self, *args, **kwargs):
        categorybpk = self.kwargs['pk']
        template_name = 'exams_app/category_form.html'
        model = models.CategoryA
        form_class = forms.CategoryAForm()
        extra_context = {
            'categorybpk': categorybpk,
            'form': form_class,
            'nav_exams': 'active',
        }
        return render(self.request, template_name, extra_context)

    def post(self, *args, **kwargs):
        categorybpk = int(self.request.POST.get('categorybpk'))

        new_categorya = models.CategoryA(
            name = self.request.POST['name'],
            description = self.request.POST['description'],
            is_ece = bool(self.request.POST.get('is_ece', False)),
            is_ee = bool(self.request.POST.get('is_ee', False)),
            is_tutorial = bool(self.request.POST.get('is_tutorial', False)),
            is_accessible = bool(self.request.POST.get('is_accessible', False)),
        )
        new_categorya.save()
        categoryb = models.CategoryB.objects.get(pk = categorybpk)
        categoryb.categoryas.add(new_categorya)
        categoryb.save()
        #return HttpResponseRedirect(reverse('exams_app:categoryb', kwargs = {'pk': categorybpk}))
        return HttpResponseRedirect(reverse('exams_app:exams_list', kwargs = {'pk': categorybpk}))

class ExamCategoryBView(View):
    def get(self, *args, **kwargs):
        template_name = 'exams_app/category_list.html'

        if not self.request.user.is_authenticated:
            categorybs = models.CategoryB.objects.all()
        else:
            #check course:
            if self.request.user.is_teacher:
                categorybs = models.CategoryB.objects.all()
            elif self.request.user.is_ece:
                categorybs = models.CategoryB.objects.filter(is_ece = True)
            elif self.request.user.is_ee:
                categorybs = models.CategoryB.objects.filter(is_ee = True)
            elif self.request.user.is_tutorial:
                categorybs = models.CategoryB.objects.filter(is_tutorial = True)
            else:
                categorybs = models.CategoryB.objects.none()

        extra_context = {
            'category_title': 'Exams',
            'categories': categorybs,
            'category_letter': 'B',
            'folder1': 'Exams',
            'nav_exams': 'active',
        }

        return render(self.request, template_name, extra_context)

class ExamCategoryAView(View):
    def get(self, *args, **kwargs):
        # categoryb = models.CategoryB.objects.get(pk = self.kwargs['pk'])
        categoryb = models.CategoryB.objects.get(pk = self.kwargs['pk'])

        if categoryb.is_accessible or self.request.user.is_teacher or self.request.user.is_staff:
            if not self.request.user.is_authenticated:
                categoryas = categoryb.categoryas.all()
            else:
                #check course:
                if self.request.user.is_teacher:
                    categoryas = categoryb.categoryas.all()
                elif self.request.user.is_ece:
                    categoryas = categoryb.categoryas.filter(is_ece = True)
                elif self.request.user.is_ee:
                    categoryas = categoryb.categoryas.filter(is_ee = True)
                elif self.request.user.is_tutorial:
                    categoryas = categoryb.categoryas.filter(is_tutorial = True)
                else:
                    categoryas = categoryb.categoryas.none()

            context = {
                'category_title': categoryb.name.title(),
                'categories': categoryas,
                'categoryb': categoryb, #this used to send the primary key of categoryb in the creadcrums
                'category_letter': 'A',
                'folder1': 'Exams',
                'folder2': categoryb.name,
                'nav_exams': 'active',
            }
            return render(self.request, 'exams_app/category_list.html', context)
        else:
            raise Http404()

class ExamListView(View):
    def get(self, *args, **kwargs):
        categorya = models.CategoryA.objects.get(pk = self.kwargs['pk'])
        categoryb = categorya.categoryb_set.get()

        if categorya.is_accessible or self.request.user.is_teacher or self.request.user.is_staff:
            if not self.request.user.is_authenticated:
                exams = categorya.exams.all()
            else:
                #check course:
                if self.request.user.is_teacher:
                    exams = categorya.exams.all()
                elif self.request.user.is_ece:
                    exams = categorya.exams.filter(is_ece = True)
                elif self.request.user.is_ee:
                    exams = categorya.exams.filter(is_ee = True)
                elif self.request.user.is_tutorial:
                    exams = categorya.exams.filter(is_tutorial = True)
                else:
                    exams = categorya.exams.none()
        else:
            raise Http404()

        context = {
            'category_title': categorya.name.title(),
            'categories': exams,
            'category_letter': 'exam',
            'categoryb': categoryb, #used to send the pk to the breadcrumb and links
            'categorya': categorya, #used to send the pk to the breadcrumb and links
            'folder1': 'Exams',
            'folder2': categoryb.name, #this is
            'folder3': categorya.name, #this is
            'nav_exams': 'active',

        }
        return render(self.request, 'exams_app/category_list.html', context)

class ExamView(View):
    def get(self, *args, **kwargs):
        categoryapk = int(self.kwargs['categoryapk'])
        exam = models.Exam.objects.get(pk = int(self.kwargs['exampk']))
        exampk = int(self.kwargs['exampk'])
        if self.request.user.is_authenticated:
            if exam.is_accessible or self.request.user.is_staff or self.request.user.is_teacher:
                ticket = models.ExamTicket.objects.create(
                    user = self.request.user,
                    date_start = datetime.now(),
                    exam = exam,
                )
                ticket.save()
                ticketpk = ticket.pk

                template_name = 'exams_app/exam_detail.html'
                context = {
                    'exam': exam,
                    'categoryapk': categoryapk,
                    'exampk': exampk,
                    'ticketpk' : ticketpk,
                    }
                return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        categoryapk = int(self.request.POST.get('categoryapk'))
        exampk = int(self.request.POST.get('exampk'))
        ticketpk = int(self.request.POST.get('ticketpk'))
        exam = models.Exam.objects.get(pk = exampk) #read only
        ticket = models.ExamTicket.objects.get(pk = ticketpk)
        score = 0

        for item in exam.items.all():
            itempk = item.pk
            for choice in item.choices.all():
                choicepk = choice.pk
                #radio buttons contain values, their values would be the pk of the choices
                if choice.correct and int(self.request.POST.get('item_' + str(itempk) + '_answer')) == int(choice.pk):
                    score = score + 1
                    ticket.answers.add(choice)
                if bool(self.request.POST.get('item_' + str(itempk) + '_choice_' + str(choicepk))):
                    ticket.answers.add(choice)

        ticket = models.ExamTicket.objects.filter(pk = ticketpk).update(
            score = score,
            items = exam.items.all().count(),
            percentage = (score / exam.items.all().count()) * 100,
            date_finish = datetime.now()
            )

        return HttpResponseRedirect(reverse('exams_app:exam_result', kwargs = {
            'categoryapk': categoryapk,
            'exampk': exampk,
            'ticketpk': ticketpk,
        }))


class ExamTicketView(View):
    def get(self, *args, **kwargs):
        categoryapk = self.kwargs['categoryapk']
        exampk = self.kwargs['exampk']
        ticketpk = self.kwargs['ticketpk']
        ticket = models.ExamTicket.objects.get(pk = ticketpk)

        template_name = 'exams_app/exam_ticket.html'
        context = {
            'ticket': ticket,
            'categoryapk': categoryapk,
            'exampk': exampk,
            'ticketpk': ticketpk,
        }

        return render(self.request, template_name, context)

class CreateExamManual(View):
    def get(self, *args, **kwargs):
        categoryapk = int(self.kwargs['pk'])
        template_name = 'exams_app/create_exam_manual.html'
        context = {
            'categoryapk': categoryapk,
        }
        return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        exam = models.Exam.objects.create(
            title = str(self.request.POST.get('title')),
            description = str(self.request.POST.get('description')),
            is_ece = bool(self.request.POST.get('is_ece')),
            is_ee = bool(self.request.POST.get('is_ee')),
            is_tutorial = bool(self.request.POST.get('is_tutorial')),
            is_accessible = bool(self.request.POST.get('is_accessible')),
            author = self.request.user,
        )
        exam.save()

        categoryapk = int(self.request.POST.get('categoryapk'))
        categorya = models.CategoryA.objects.get(pk = categoryapk)
        categorya.exams.add(exam)
        return HttpResponseRedirect(reverse('exams_app:create_exam_manual_add_item', kwargs = {'exampk': exam.pk, 'categoryapk': categoryapk,}))

class CreateExamManualAddItem(View):
    def get(self, *args, **kwargs):
        template_name = 'exams_app/exam_form.html'
        exampk = int(self.kwargs['exampk'])
        exam = models.Exam.objects.get(pk = exampk)

        categoryapk = int(self.kwargs['categoryapk'])
        context = {
            'exampk': exampk,
            'categoryapk': categoryapk,
            'exam': exam,
        }
        return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        exampk = int(self.request.POST.get('exampk'))
        categoryapk = int(self.request.POST.get('categoryapk'))

        try:
            question = models.MCQ.objects.create(
                question = self.request.POST.get('question'),
                image = self.request.FILES['image'],
                )
        except:
            question = models.MCQ.objects.create(
                question = self.request.POST.get('question'),
            )
        question.save()

        letters = ['a', 'b', 'c', 'd']
        for letter in letters:
            try:
                choice = models.Choice.objects.create(
                    content = self.request.POST.get('choice_' + letter),
                    correct = bool(self.request.POST.get('choice_' + letter + '_correct')),
                    image = self.request.FILES['choice_' + letter + '_image'],
                    explanation = self.request.POST.get('choice_' + letter + '_explanation'),
                )

            except:
                choice = models.Choice.objects.create(
                    content = self.request.POST.get('choice_' + letter ),
                    correct = bool(self.request.POST.get('choice_' + letter + '_correct')),
                    explanation = self.request.POST.get('choice_' + letter + '_explanation'),
                )
            choice.save()
            question.choices.add(choice)

        exam = models.Exam.objects.get(pk = exampk)
        exam.items.add(question)

        return HttpResponseRedirect(reverse('exams_app:create_exam_manual_add_item', kwargs = {'exampk': exampk, 'categoryapk': categoryapk,}))

class ExamCategoryAUpdate(UpdateView):
    template_name = 'exams_app/category_form.html'
    model = models.CategoryA
    fields = '__all__'
    success_url = reverse_lazy('exams_app:exams')
    extra_context = {'nav_exams': 'active',}

class ExamCategoryBUpdate(UpdateView):
    template_name = 'exams_app/category_form.html'
    model = models.CategoryB
    fields = '__all__'
    success_url = reverse_lazy('exams_app:exams')
    extra_context = {'nav_exams': 'active',}

class UpdateExamView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_staff or self.request.user.is_teacher:
                categoryapk = int(self.kwargs['categoryapk'])
                exampk = int(self.kwargs['exampk'])
                template_name = 'exams_app/update_exam.html'
                exam = models.Exam.objects.get(pk = exampk)
                context = {
                    'categoryapk': categoryapk,
                    'exampk': exampk,
                    'exam': exam,
                }
                return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        categoryapk = int(self.request.POST.get('categoryapk'))
        return HttpResponseRedirect(reverse('exams_app:exams_list', kwargs = {
            'pk': categoryapk,
        }))


class DeleteItemView(View):
    def get(self, *args, **kwargs):
        itempk = int(self.kwargs['itempk'])
        categoryapk = int(self.kwargs['categoryapk'])
        exampk = int(self.kwargs['exampk'])

        item = models.MCQ.objects.get(pk = itempk)
        item.delete()

        return HttpResponseRedirect(reverse('exams_app:update_exam', kwargs = {
            'categoryapk': categoryapk,
            'exampk': exampk,
        }))

class UpdateExamManualAddItemView(View):
    def get(self, *args, **kwargs):
        template_name = 'exams_app/exam_form.html'
        exampk = int(self.kwargs['exampk'])
        exam = models.Exam.objects.get(pk = exampk)

        categoryapk = int(self.kwargs['categoryapk'])
        context = {
            'exampk': exampk,
            'categoryapk': categoryapk,
            'exam': exam,
        }
        return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        exampk = int(self.request.POST.get('exampk'))
        categoryapk = int(self.request.POST.get('categoryapk'))

        try:
            question = models.MCQ.objects.create(
                question = self.request.POST.get('question'),
                image = self.request.FILES['image'],
                )
        except:
            question = models.MCQ.objects.create(
                question = self.request.POST.get('question'),
            )
        question.save()

        letters = ['a', 'b', 'c', 'd']
        for letter in letters:
            try:
                choice = models.Choice.objects.create(
                    content = self.request.POST.get('choice_' + letter),
                    correct = bool(self.request.POST.get('choice_' + letter + '_correct')),
                    image = self.request.FILES['choice_' + letter + '_image'],
                    explanation = self.request.POST.get('choice_' + letter + '_explanation'),
                )

            except:
                choice = models.Choice.objects.create(
                    content = self.request.POST.get('choice_' + letter ),
                    correct = bool(self.request.POST.get('choice_' + letter + '_correct')),
                    explanation = self.request.POST.get('choice_' + letter + '_explanation'),
                )
            choice.save()
            question.choices.add(choice)

        exam = models.Exam.objects.get(pk = exampk)
        exam.items.add(question)

        return HttpResponseRedirect(reverse('exams_app:update_exam', kwargs = {'exampk': exampk, 'categoryapk': categoryapk,}))


class ExamCategoryADelete(DeleteView):
    template_name = 'exams_app/confirm_delete.html'
    model = models.CategoryA
    success_url = reverse_lazy('exams_app:exams')
    extra_context = {'nav_exams': 'active',}

class ExamCategoryBDelete(DeleteView):
    template_name = 'exams_app/confirm_delete.html'
    model = models.CategoryB
    success_url = reverse_lazy('exams_app:exams')
    extra_context = {'nav_exams': 'active',}

class DeleteExamView(DeleteView):
    template_name = 'exams_app/confirm_delete.html'
    model = models.Exam
    success_url = reverse_lazy('exams_app:exams')
    extra_context = {'nav_exams': 'active',}

class CreateExamUploadView(View):
    def get(self, *args, **kwargs):
        pk = int(self.kwargs['pk'])
        template_name = 'exams_app/exam_create_upload.html'
        return render(self.request, template_name, {'pk': pk})

    def post(self, *args, **kwarg):

        pk = self.request.POST.get('pk')
        file = self.request.FILES['examfile']
        new_exam = models.Exam(
            title = self.request.POST.get('title'),
            description = self.request.POST.get('description'),
            author = self.request.user,
            is_ece = bool(self.request.POST.get('is_ece')),
            is_ee = bool(self.request.POST.get('is_ee')),
            is_tutorial = bool(self.request.POST.get('is_tutorial')),
            is_accessible = bool(self.request.POST.get('is_accessible'))
        )
        new_exam.save()

        wb = load_workbook(file, read_only = True)
        sheetnames = wb.sheetnames #this is a list of sheetnames
        ws = wb[sheetnames[0]] #ill just take the first whatever the first sheet is

        mcqs = [] #this will be the container for the mcqs for the bulk create later

        for row in ws.rows:
            new_mcq = models.MCQ(
                question = row[0].value,
            )
            new_mcq.save()

            for col in range(1, 5):
                if '##' in row[col].value:
                    correct = True
                else:
                    correct = False

                new_choice = models.Choice(
                    content = row[col].value,
                    correct = correct,
                )
                new_choice.save()
                new_mcq.choices.add(new_choice)
            new_exam.items.add(new_mcq)

        categorya = models.CategoryA.objects.get(pk = pk)
        categorya.exams.add(new_exam)

        return HttpResponseRedirect(reverse('exams_app:exams_list', kwargs = {'pk':categorya.pk}))
