from django.urls import path
from . import views
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import cache_page


app_name = 'exams_app_2'

urlpatterns = [
    # path('categorybs', views.ExamCategoryBView.as_view(), name = 'exams'),
    path('exams_list', views.ExamList.as_view(), name = 'exam_list'),
    path('add_exam', views.AddExam.as_view(), name = 'add_exam'),
    #path('detail/<exampk>', views.ExamDetail.as_view(), name='exam_detail'),
    path('delete/<exampk>', views.ExamDelete.as_view(), name='exam_delete'),
    path('submit/<exampk>', views.ExamSubmit.as_view(), name='submit'),
    path('download/<filepk>', views.FileDownload.as_view(), name='exam_download'),
    path('detail/<exampk>', views.ExamDetail.as_view(), name='exam_detail'),
    path('file/<exampk>', views.AddExamFile.as_view(), name='file'),
    path('result/<exampk>/<answersheetpk>', views.ExamResult.as_view(), name='result'),
    path('delete_sheet/<answersheetpk>/<userpk>', views.SheetDelete.as_view(), name='sheet_delete'),
    path('lock/<exampk>', views.ExamLock.as_view(), name='exam_lock'),
    path('unlock/<exampk>', views.ExamUnlock.as_view(), name='exam_unlock'),
    path('showanswerkey/<exampk>', views.ExamShowAnswerKey.as_view(), name='exam_done'),
    path('hideanswerkey/<exampk>', views.ExamHideAnswerKey.as_view(), name='exam_undone'),
]
