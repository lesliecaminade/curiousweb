from django.urls import path
from . import views
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import cache_page


app_name = 'exams_app'

urlpatterns = [
    # path('categorybs', views.ExamCategoryBView.as_view(), name = 'exams'),
    # path('categoryas/<pk>', views.ExamCategoryAView.as_view(), name='categorya'),
    #path('exams_list/<pk>', views.ExamListView.as_view(), name='categoryb'),
    # path('exams_list/<pk>', views.ExamListView.as_view(), name='exams_list'),
    # path('exam/<exampk>', views.ExamView.as_view(), name='exam'),
    # path('exam/result/<categoryapk>/<exampk>/<ticketpk>', views.ExamTicketView.as_view(), name='exam_result'),
    #
    # path('create/categorya/<pk>', views.ExamCategoryACreate.as_view(), name='create_categorya'),
    # path('create/categoryb', views.ExamCategoryBCreate.as_view(), name='create_categoryb'),
    # path('create/exam/manual/<pk>', views.CreateExamManual.as_view(), name='create_exam_manual'),
    # path('create/exam/manual/additem/<categoryapk>/<exampk>', views.CreateExamManualAddItem.as_view(), name='create_exam_manual_add_item'),


    # path('update/categorya/<pk>', views.ExamCategoryAUpdate.as_view(), name='update_categorya'),
    # path('update/categoryb/<pk>', views.ExamCategoryBUpdate.as_view(), name='update_categoryb'),
    # path('update/exam/<categoryapk>/<exampk>', views.UpdateExamView.as_view(), name='update_exam'),
    # path('update/exam/additem/<categoryapk>/<exampk>', views.UpdateExamManualAddItemView.as_view(), name='update_exam_add_item'),
    # path('update/exam/deleteitem/<categoryapk>/<exampk>/<itempk>', views.DeleteItemView.as_view(), name='delete_item'),


    # path('delete/categorya/<pk>', views.ExamCategoryADelete.as_view(), name='delete_categorya'),
    # path('delete/categoryb/<pk>', views.ExamCategoryBDelete.as_view(), name='delete_categoryb'),
    # path('delete/exam/<pk>', views.DeleteExamView.as_view(), name='delete_exam'),
    # path('upload/exam/<pk>', views.CreateExamUploadView.as_view(), name='create_exam_upload'),
    #-------------------------second remake----------------------------------------------------------
    path('all', views.MCQList.as_view(), name='all'),
    path('exam/<pk>', views.ExamView.as_view(), name='exam'),
    path('create/exam/manual', views.CreateExamManual.as_view(), name='create_exam_manual'),
    path('create/exam/manual/additem/<pk>', views.CreateExamManualAddItem.as_view(), name='create_exam_manual_add_item'),
    path('upload/exam/', views.CreateExamUploadView.as_view(), name='create_exam_upload'),
    path('delete/exam/<pk>', views.DeleteExamView.as_view(), name='delete_exam'),
    path('lock/exam/<pk>', views.LockExamView.as_view(), name='lock_exam'),
    path('unlock/exam/<pk>', views.UnlockExamView.as_view(), name='unlock_exam'),

]
