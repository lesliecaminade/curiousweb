from django.urls import path
from . import views
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import cache_page


app_name = 'exams_app_3'

urlpatterns = [
    path('all', views.MCQList.as_view(), name='all'),
    path('exam/<pk>', views.ExamView.as_view(), name='exam'),
    path('create/exam/manual', views.CreateExamManual.as_view(), name='create_exam_manual'),
    path('create/exam/manual/additem/<pk>', views.CreateExamManualAddItem.as_view(), name='create_exam_manual_add_item'),
    path('upload/exam/', views.CreateExamUploadView.as_view(), name='create_exam_upload'),
    path('delete/exam/<pk>', views.DeleteExamView.as_view(), name='delete_exam'),
    path('lock/exam/<pk>', views.LockExamView.as_view(), name='lock_exam'),
    path('unlock/exam/<pk>', views.UnlockExamView.as_view(), name='unlock_exam'),
    path('toggle/<flag>/<pk>/<setting>', views.ToggleFlag.as_view(), name='toggle_flag'),
    path('delete/item/<pk>/<exampk>', views.DeleteItem.as_view(), name='delete_item'),
    path('edit/item/<pk>/<exampk>', views.EditItem.as_view(), name='edit_item'),

]
