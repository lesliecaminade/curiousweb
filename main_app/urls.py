from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'main_app'

urlpatterns = [
    path('enroll/', views.EnrollView.as_view(), name = 'enroll'),
    path('register/', views.RegisterView.as_view(), name = 'register')
]
