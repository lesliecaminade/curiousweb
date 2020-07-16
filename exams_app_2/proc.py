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
from .image_helpers import Thumbnail


def compute_stats(exampk):
    if self.request.user.is_superuser:
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
            
        return {'percent_as': percent_as, 'percent_bs': percent_bs, 'percent_cs': percent_cs, 'percent_ds': percent_ds, 'percent_corrects': percent_corrects, 'item_labels': item_labels}
