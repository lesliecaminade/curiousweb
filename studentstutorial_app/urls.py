from django.urls import path
from . import views

app_name = 'studentstutorial_app'

urlpatterns = [
    path('',views.StudentTutorialListViewAll.as_view(),name='list'),
    path('all/',views.StudentTutorialListViewAll.as_view(), name='list_all'),
    path('enrolled/true/',views.StudentTutorialListViewEnrolled.as_view(), name='list_enrolled_true'),
    path('enrolled/false/',views.StudentTutorialListViewNotEnrolled.as_view(), name='list_enrolled_false'),
    path('<int:pk>/',views.StudentTutorialDetailView.as_view(),name='detail'),
    path('create/',views.StudentTutorialCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.StudentTutorialUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.StudentTutorialDeleteView.as_view(),name='delete'),
    path('success/', views.StudentTutorialSuccessEnrollment.as_view(),name='success'),
    path('fail/', views.StudentTutorialFailEnrollment.as_view(),name='fail'),
]
