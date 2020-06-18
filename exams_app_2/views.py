from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                DeleteView, CreateView,
                                UpdateView)
from . import models
from . import forms

from datetime import datetime
from communications.standard_email import send_email
from .image_helpers import resize_image_field
# Create your views here.

class ExamList(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                exams = models.Exam.objects.all().order_by('-pk')
            elif self.request.user.is_ece:
                exams = models.Exam.objects.filter(is_ece = True).order_by('-pk')
            elif self.request.user.is_ee:
                exams = models.Exam.objects.filter(is_ee = True).order_by('-pk')
            elif self.requets.user.is_tutorial:
                exams = models.Exam.objects.filter(is_tutorial = True).order_by('-pk')
            else:
                send_email(curiousweb.settings.ADMIN_EMAILS, 'SITE ERROR REPORT',
                f"""Unhandled user type at exams_app_2.views.ExamList""")
                exams = models.Exam.objects.all().order_by('-pk')

            template_name = 'exams_app_2/exams_list.html'
            context = {
                'exams': exams,
            }

            return render(self.request, template_name, context)

class AddExam(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            template_name = 'exams_app_2/exam_form.html'
            exam_form = forms.ExamForm
            context = {
                'exam_form': exam_form,
                'answer_key_looper': [i for i in range(1,101)],
                'number_of_files': [i for i in range(6)],
            }
            return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        if self.request.user.is_superuser:

            new_answer_key = models.AnswerKey()
            new_answer_key.save()

            for i in range(1,101):
                new_item = models.Item(
                    item_number = i,
                    answer = self.request.POST.get('answer_' + str(i), 'no answer'),
                    bonus = False,
                    skip = False,
                )
                new_item.save()
                new_answer_key.items.add(new_item)

            new_exam = models.Exam(
                name = self.request.POST.get('name'),
                description = self.request.POST.get('description'),
                is_ece = bool(self.request.POST.get('is_ece', False)),
                is_ee = bool(self.request.POST.get('is_ee', False)),
                is_tutorial = bool(self.request.POST.get('is_tutorial', False)),
                is_accessible = bool(self.request.POST.get('is_accessible', False)),
                thumbnail = self.request.FILES.get('thumbnail'),
                answer_key = new_answer_key,
                timestamp = datetime.now(),
            )
            new_exam.save()
            resize_image_field(new_exam.thumbnail, height = 300)

            for i in range(6):
                if self.request.FILES.get('exam_file_' + str(i)):
                    new_examfile = models.ExamFile(
                        name = 'Page ' + str(i),
                        file = self.request.FILES.get('exam_file_' + str(i)),
                        is_ece = bool(self.request.POST.get('is_ece', False)),
                        is_ee = bool(self.request.POST.get('is_ee', False)),
                        is_tutorial = bool(self.request.POST.get('is_tutorial', False)),
                        is_accessible = bool(self.request.POST.get('is_accessible', False)),
                    )
                    new_examfile.save()
                    new_exam.files.add(new_examfile)

            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'exams',}))

class ExamDetail(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            exampk = int(self.kwargs.get('exampk'))
            exam = models.Exam.objects.get(pk = exampk)

            percent_as = []
            percent_bs = []
            percent_cs = []
            percent_ds = []
            percent_corrects = []
            item_labels = []

            for i in range(1,101):
                count_a = 0
                count_b = 0
                count_c = 0
                count_d = 0
                count_correct = 0
                for sheet in exam.answer_sheets.all():
                    for item in sheet.items.filter(item_number = i):
                        if item.answer == 'a':
                            count_a = count_a + 1
                        elif item.answer == 'b':
                            count_b = count_b + 1
                        elif item.answer == 'c':
                            count_c = count_c + 1
                        elif item.answer == 'd':
                            count_d = count_d + 1
                        else:
                            pass

                        answer = exam.answer_key.items.filter(item_number = i)[0].answer
                        if item.answer == answer:
                            count_correct = count_correct + 1

                total = count_a + count_b + count_c + count_d
                percent_as.append(int(count_a * 100/ total))
                percent_bs.append(int(count_b * 100/ total))
                percent_cs.append(int(count_c * 100/ total))
                percent_ds.append(int(count_d * 100/ total))
                percent_corrects.append(int(count_correct * 100/ total))


            i = 1
            for item in exam.answer_key.items.all():
                item_labels.append(str(i) + ', '+ str(item.answer))
                i = i + 1

            context = {
                'exam': exam,
                'exampk': exampk,
                'percent_as': percent_as,
                'percent_bs': percent_bs,
                'percent_cs': percent_cs,
                'percent_ds': percent_ds,
                'percent_corrects': percent_corrects,
                'item_labels': item_labels,
            }
            template_name = 'exams_app_2/exam_detail.html'
            return render(self.request, template_name, context)

class ExamDelete(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            exam = models.Exam.objects.get(pk = self.kwargs.get('exampk'))
            exam.delete()
            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'exams',}))

class ExamDownload(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            exam = models.Exam.objects.get(pk = self.kwargs.get('exampk'))

            if exam.is_accessible and ((self.request.user.is_ece and exam.is_ece) or (self.request.user.is_ee and exam.is_ee) or (self.request.user.is_tutorial and exam.is_tutorial)) :
                filename = exam.file.name.split('/')[-1]
                response = HttpResponse(exam.file, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename=%s' % filename
                return response
            else:
                return HttpResponse('Sorry, download not accessible.')

class ExamSubmit(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            exampk = int(self.kwargs.get('exampk'))
            exam = models.Exam.objects.get(pk = self.kwargs.get('exampk'))
            has_taken = bool(exam.answer_sheets.filter(user = self.request.user).exists())
            context = {
                'exam': exam,
                'has_taken': has_taken,
                'exampk': exampk,
                'answer_key_looper': [i for i in range(1,101)]
            }
            template_name = 'exams_app_2/answer_sheet_base.html'
            return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:

            exam = models.Exam.objects.get(pk = int(self.request.POST.get('exampk')))
            has_taken = bool(exam.answer_sheets.filter(user = self.request.user).exists())

            new_answer_sheet = models.AnswerSheet(
                user = self.request.user,
                date_submitted = datetime.today(),
                first_take = not has_taken,
            )
            new_answer_sheet.save()

            score = 0
            items = 100

            for i in range(1, 101):
                new_item = models.Item(
                    item_number = i,
                    answer = self.request.POST.get('answer_' + str(i), 'no answer'),
                    bonus = False,
                    skip = False,
                )
                new_item.save()

                if self.request.POST.get('answer_' + str(i), 'no answer') == exam.answer_key.items.get(item_number = i).answer:
                    score = score + 1

                new_answer_sheet.items.add(new_item)

            models.AnswerSheet.objects.filter(pk = new_answer_sheet.pk).update(
                score = score,
                percentage = (score/items) * 100,
                )

            exam.answer_sheets.add(new_answer_sheet)

            return HttpResponseRedirect(reverse('exams_app_2:result', kwargs = {
                'answersheetpk': new_answer_sheet.pk,
                'exampk': exam.pk,
            }))

class ExamResult(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            template_name = 'exams_app_2/result.html'
            answersheetpk = int(self.kwargs.get('answersheetpk'))
            exampk = int(self.kwargs.get('exampk'))
            answer_sheet = models.AnswerSheet.objects.get(pk = answersheetpk)
            exam = models.Exam.objects.get(pk = exampk)
            prev_answer_sheets = exam.answer_sheets.filter(user = self.request.user)

            context = {
                'answer_sheet': answer_sheet,
                'exam': exam,
                'prev_answer_sheets': prev_answer_sheets,
            }
            return render(self.request, template_name, context)

class AddExamFile(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            template_name = 'exams_app_2/addfile.html'
            exampk = int(self.kwargs.get('exampk'))
            form = forms.FileForm

            context = {
                'exampk': exampk,
                'form': form,
            }
            return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        if self.request.user.is_superuser:
            exampk = int(self.request.POST.get('exampk'))
            exam = models.Exam.objects.get(pk = exampk)

            try:
                file = self.request.FILES['file']
            except:
                return HttpResponseRedirect(reverse('exams_app_2:file', kwargs = {'exampk': exampk, }))

            new_examfile = models.ExamFile(
                name = self.request.POST.get('name'),
                file = file,
                is_ece = exam.is_ece,
                is_ee = exam.is_ee,
                is_tutorial = exam.is_tutorial,
                is_accessible = exam.is_accessible,
            )
            new_examfile.save()

            exam.files.add(new_examfile)

            return HttpResponseRedirect(reverse('exams_app_2:exam_detail', kwargs = {'exampk': exampk,}))

class FileDownload(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            file = models.ExamFile.objects.get(pk = self.kwargs.get('filepk'))
            if file.is_accessible:
                filename = file.file.name.split('/')[-1]
                response = HttpResponse(file.file, content_type='text/plain')
                response['Content-Disposition'] = 'attachment; filename=%s' % filename
                return response
            else:
                return HttpResponse('Sorry, download not accessible.')

class SheetDelete(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            sheet = models.AnswerSheet.objects.get(pk = self.kwargs.get('answersheetpk'))
            userpk = int(self.kwargs.get('userpk'))
            sheet.delete()
            return HttpResponseRedirect(reverse('main_app:user', kwargs = {'pk': userpk,}))

class ExamLock(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            exam = models.Exam.objects.filter(pk = int(self.kwargs.get('exampk'))).update(is_accessible=False, is_done = False)
            exam = models.Exam.objects.get(pk = int(self.kwargs.get('exampk')))
            exam.files.all().update(is_accessible = False)
            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'exams',}))

class ExamUnlock(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            exam = models.Exam.objects.filter(pk = int(self.kwargs.get('exampk'))).update(is_accessible=True, is_done = False)
            exam = models.Exam.objects.get(pk = int(self.kwargs.get('exampk')))
            exam.files.all().update(is_accessible = True)

            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'exams',}))

class ExamShowAnswerKey(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            exam = models.Exam.objects.filter(pk = int(self.kwargs.get('exampk'))).update(is_done=True)
            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'exams',}))

class ExamHideAnswerKey(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_superuser:
            exam = models.Exam.objects.filter(pk = int(self.kwargs.get('exampk'))).update(is_done=False)
            return HttpResponseRedirect(reverse('index', kwargs = {'activetab': 'exams',}))


class ExamStats(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            exampk = int(self.kwargs.get('exampk'))
            exam = models.Exam.objects.get(pk = exampk)

            percent_as = []
            percent_bs = []
            percent_cs = []
            percent_ds = []
            percent_corrects = []
            item_labels = []

            for i in range(1,101):
                count_a = 0
                count_b = 0
                count_c = 0
                count_d = 0
                count_correct = 0
                for sheet in exam.answer_sheets.all():
                    for item in sheet.items.filter(item_number = i):
                        if item.answer == 'a':
                            count_a = count_a + 1
                        elif item.answer == 'b':
                            count_b = count_b + 1
                        elif item.answer == 'c':
                            count_c = count_c + 1
                        elif item.answer == 'd':
                            count_d = count_d + 1
                        else:
                            pass

                        answer = exam.answer_key.items.filter(item_number = i)[0].answer
                        if item.answer == answer:
                            count_correct = count_correct + 1

                total = count_a + count_b + count_c + count_d
                percent_as.append(int(count_a * 100/ total))
                percent_bs.append(int(count_b * 100/ total))
                percent_cs.append(int(count_c * 100/ total))
                percent_ds.append(int(count_d * 100/ total))
                percent_corrects.append(int(count_correct * 100/ total))


            i = 1
            for item in exam.answer_key.items.all():
                item_labels.append(str(i) + ', '+ str(item.answer))
                i = i + 1

            context = {
                'exam': exam,
                'exampk': exampk,
                'percent_as': percent_as,
                'percent_bs': percent_bs,
                'percent_cs': percent_cs,
                'percent_ds': percent_ds,
                'percent_corrects': percent_corrects,
                'item_labels': item_labels,
            }
            template_name = 'exams_app_2/exam_stats.html'
            return render(self.request, template_name, context)
