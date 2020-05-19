from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
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

class ExamCategoryBCreate(CreateView):
    template_name = 'exams_app/category_form.html'
    model = models.CategoryB
    fields = '__all__'
    success_url = reverse_lazy('exams_app:exams')
    extra_context = {
        'nav_exams': 'active',
    }

class ExamCategoryACreate(View):

    success_url = reverse_lazy('exams_app:exams')

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
        categorybpk = int(self.request.POST['categorybpk'])

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
            'category_title': 'Main Categories',
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

class ExamListView(View):
    def get(self, *args, **kwargs):
        categorya = models.CategoryA.objects.get(pk = self.kwargs['pk'])
        categoryb = categorya.categoryb_set.get()

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

    def post():
        pass

class ExamView(View):
    def get(self, *args, **kwargs):
        exam = models.Exam.objects.get(pk = self.kwargs['pk'])
        items = list(exam.items.all())
        number_of_items = len(items)
        context = {
            'exam': exam,
            'items': items,
            'number_of_items': number_of_items,
            'exam_pk': self.kwargs['pk'],
            'nav_exams': 'active',
        }
        return render(self.request, 'exams_app/exam_detail.html', context)

    def post(self, *args, **kwargs):
        #answers in self.request.POST['question_n_selected_answer']
        #with values ranging from 1 to 4
        exam_pk = self.request.POST.get('exam_pk')
        exam = models.Exam.objects.get(pk = exam_pk)
        items = exam.items.all()

        selected_answers = []

        number_of_items = int(self.request.POST['number_of_items'])
        for i in range(1, number_of_items + 1):
            try:
                name_to_query = f"""question_{i}_selected_answer"""
                selected_answers.append(self.request.POST[name_to_query])
            except:
                selected_answers.append(99) #99 means no answer

        counter = 0
        correct_answer_count = 0
        for item in items:
            if item.correct1 == True and int(selected_answers[counter]) == 1:
                #compare the selected answers to the correct answers
                correct_answer_count = correct_answer_count + 1

            if item.correct2 == True and int(selected_answers[counter]) == 2:
                #compare the selected answers to the correct answers
                correct_answer_count = correct_answer_count + 1

            if item.correct3 == True and int(selected_answers[counter]) == 3:
                #compare the selected answers to the correct answers
                correct_answer_count = correct_answer_count + 1

            if item.correct4 == True and int(selected_answers[counter]) == 4:
                #compare the selected answers to the correct answers
                correct_answer_count = correct_answer_count + 1
            counter = counter + 1


        ticket = models.ExamTicket.objects.create(
            exam = exam,
            date_taken = make_aware(datetime.now()),
            score = correct_answer_count,
            percentage = round((correct_answer_count / number_of_items) * 100,2),
            user = self.request.user,
            items = number_of_items,
        )

        return HttpResponseRedirect(reverse('exams_app:exam_result', kwargs = {'pk': ticket.pk}))

class ExamTicketView(DetailView):
    template_name = 'exams_app/exam_ticket.html'
    model = models.ExamTicket
    context_object_name = 'ticket'
    extra_context = {'nav_exams': 'active',}


class CreateExamSuccessView(TemplateView):
    extra_context = {'nav_exams': 'active',}
    template_name = 'exams_app/exam_create_success.html'

class CreateExamItemsAskView(View):
    def get(self, *args, **kwargs):
        categoryapk = self.kwargs['pk']
        template_name = 'exams_app/exam_create_items_ask.html'
        context = {
            'categoryapk': categoryapk,
            'nav_exams': 'active',
        }
        return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        categoryapk = self.request.POST.get('categoryapk')
        items = int(self.request.POST.get('items'))
        return HttpResponseRedirect(reverse('exams_app:create_exam', kwargs = {'items': items, 'pk': categoryapk,}))

class CreateExamView(View):
    def get(self, *args, **kwargs):
        template_name = 'exams_app/exam_form.html'
        if self.kwargs['items'] is not None:
            #if the previous page specified number of items
            items = int(self.kwargs['items'])
        else:
            items = 100

        categorya_pk = self.kwargs['pk']

        context = {
            'items': [i for i in range(1, items + 1)],
            'categorya_pk': categorya_pk,
            'nav_exams': 'active',
        }
        return render(self.request, template_name, context)

    def post(self, *args, **kwargs):

        mcq_ids = []
        #this will be a temporary container for the ids
        #of the mcqs that will be created
        title = self.request.POST.get('title')
        description = self.request.POST.get('description')
        items = int(self.kwargs['items'])
        categorya_pk = int(self.request.POST.get('categorya_pk'))

        new_exam = models.Exam(
            title = title,
            description = description,
            author = self.request.user,
            is_ece = bool(self.request.POST.get('is_ece')),
            is_ee = bool(self.request.POST.get('is_ee')),
            is_tutorial = bool(self.request.POST.get('is_tutorial')),
            is_accessible = bool(self.request.POST.get('is_accessible'))
        )
        new_exam.save()

        categorya = models.CategoryA.objects.get(pk = categorya_pk)
        categorya.exams.add(new_exam)

        #create an mcq instance for every mcq created on the form
        for i in range(1, items + 1):
            question = self.request.POST['question_' + str(i)]
            correct = int(self.request.POST['question_' + str(i) + '_choice_correct'])

            correct1 = False
            correct2 = False
            correct3 = False
            correct4 = False

            if correct == 1:
                correct1 = True
            elif correct == 2:
                correct2 = True
            elif correct == 3:
                correct3 == True
            elif correct == 4:
                correct4 == True

            choice1 = self.request.POST['question_' + str(i) + '_choice_1']
            choice2 = self.request.POST['question_' + str(i) + '_choice_2']
            choice3 = self.request.POST['question_' + str(i) + '_choice_3']
            choice4 = self.request.POST['question_' + str(i) + '_choice_4']

            explanation = self.request.POST['question_' + str(i) + '_explanation']

            try:
                image = self.request.FILES['question_' + str(i) + '_main_image']
            except:
                image = None
            try:
                image1 = self.request.FILES['question_' + str(i) + '_choice_1_image']
            except:
                image1 = None
            try:
                image2 = self.request.FILES['question_' + str(i) + '_choice_2_image']
            except:
                image2 = None
            try:
                image3 = self.request.FILES['question_' + str(i) + '_choice_3_image']
            except:
                image3 = None
            try:
                image4 = self.request.FILES['question_' + str(i) + '_choice_4_image']
            except:
                image4 = None

            new_mcq = models.MCQ(
                question = question,
                choice1 = choice1,
                choice2 = choice2,
                choice3 = choice3,
                choice4 = choice4,
                explanation = explanation,
                correct1 = correct1,
                correct2 = correct2,
                correct3 = correct3,
                correct4 = correct4,
                image = image,
                image1 = image1,
                image2 = image2,
                image3 = image3,
                image4 = image4,
            )


            #also add and save the question to the new_exam
            new_mcq.save()
            new_exam.items.add(new_mcq)

        #finally commit the saves to the database
        new_exam.save()
        categorya.save()

        return HttpResponseRedirect(reverse('exams_app:exams_list', kwargs = {'pk':categorya.pk}))

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

class UpdateExamView(UpdateView):
    template_name = 'exams_app/category_form.html'
    model = models.Exam
    fields = '__all__'
    success_url = reverse_lazy('exams_app:exams')
    extra_context = {'nav_exams': 'active',}

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
