from django.urls import path
from . import views
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import cache_page


app_name = 'exams_app'

urlpatterns = [
    path('categorybs', views.ExamCategoryBView.as_view(), name = 'exams'),
    path('categoryas/<pk>', views.ExamCategoryAView.as_view(), name='categorya'),
    #path('exams_list/<pk>', views.ExamListView.as_view(), name='categoryb'),
    path('exams_list/<pk>', views.ExamListView.as_view(), name='exams_list'),
    path('exam/<pk>', views.ExamView.as_view(), name='exam'),

    path('exam/result/<pk>', views.ExamTicketView.as_view(), name='exam_result'),

    path('create/categorya/<pk>', views.ExamCategoryACreate.as_view(), name='create_categorya'),
    path('create/categoryb', views.ExamCategoryBCreate.as_view(), name='create_categoryb'),
    path('create/exam/<items>/<pk>', views.CreateExamView.as_view(), name='create_exam'),
    path('create/ask/<pk>', views.CreateExamItemsAskView.as_view(), name='create_exam_items_ask'),


    path('update/categorya/<pk>', views.ExamCategoryAUpdate.as_view(), name='update_categorya'),
    path('update/categoryb/<pk>', views.ExamCategoryBUpdate.as_view(), name='update_categoryb'),
    path('update/exam/<pk>', views.UpdateExamView.as_view(), name='update_exam'),

    path('delete/categorya/<pk>', views.ExamCategoryADelete.as_view(), name='delete_categorya'),
    path('delete/categoryb/<pk>', views.ExamCategoryBDelete.as_view(), name='delete_categoryb'),
    path('delete/exam/<pk>', views.DeleteExamView.as_view(), name='delete_exam'),

]
