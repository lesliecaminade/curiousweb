from django.urls import path
from . import views

app_name = 'studentsece_app'

urlpatterns = [
    path('',views.StudentECEListViewAll.as_view(),name='list'),
    path('all/',views.StudentECEListViewAll.as_view(), name='list_all'),
    path('enrolled/true/',views.StudentECEListViewEnrolled.as_view(), name='list_enrolled_true'),
    path('enrolled/false/',views.StudentECEListViewNotEnrolled.as_view(), name='list_enrolled_false'),
    path('<int:pk>/',views.StudentECEDetailView.as_view(),name='detail'),
    path('create/',views.StudentECECreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.StudentECEUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.StudentECEDeleteView.as_view(),name='delete'),
    path('success/', views.StudentECESuccessEnrollment.as_view(),name='success'),
    path('fail/', views.StudentECEFailEnrollment.as_view(),name='fail'),
]
