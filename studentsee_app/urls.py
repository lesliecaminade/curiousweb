from django.urls import path
from . import views

app_name = 'studentsee_app'

urlpatterns = [
    path('',views.StudentEEListViewAll.as_view(),name='list'),
    path('all/',views.StudentEEListViewAll.as_view(), name='list_all'),
    path('enrolled/true/',views.StudentEEListViewEnrolled.as_view(), name='list_enrolled_true'),
    path('enrolled/false/',views.StudentEEListViewNotEnrolled.as_view(), name='list_enrolled_false'),
    path('<int:pk>/',views.StudentEEDetailView.as_view(),name='detail'),
    path('create/',views.StudentEECreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.StudentEEUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.StudentEEDeleteView.as_view(),name='delete'),
    path('success/', views.StudentEESuccessEnrollment.as_view(),name='success'),
    path('fail/', views.StudentEEFailEnrollment.as_view(),name='fail'),
]
