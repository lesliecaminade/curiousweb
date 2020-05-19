from django.urls import path
from . import views

app_name = 'students_app_1'

urlpatterns = [
    path('',views.StudentListViewAll.as_view(),name='list'),
    path('all/',views.StudentListViewAll.as_view(), name='list_all'),
    path('enrolled/true/',views.StudentListViewEnrolled.as_view(), name='list_enrolled_true'),
    path('enrolled/false/',views.StudentListViewNotEnrolled.as_view(), name='list_enrolled_false'),
    path('<int:pk>/',views.StudentDetailView.as_view(),name='detail'),
    path('create/',views.StudentCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.StudentUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.StudentDeleteView.as_view(),name='delete'),
    path('success/', views.StudentSuccessEnrollment.as_view(),name='success'),
    path('fail/', views.StudentFailEnrollment.as_view(),name='fail'),
]
