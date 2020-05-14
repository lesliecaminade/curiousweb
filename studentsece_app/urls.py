from django.urls import path
from . import views

app_name = 'studentsece_app'

urlpatterns = [
    path('',views.StudentECEListView.as_view(),name='list'),
    path('<int:pk>/',views.StudentECEDetailView.as_view(),name='detail'),
    path('create/',views.StudentECECreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.StudentECEUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.StudentECEDeleteView.as_view(),name='delete'),
    path('success/', views.StudentECESuccessEnrollment.as_view(),name='success'),
]
