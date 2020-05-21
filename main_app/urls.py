from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'main_app'

urlpatterns = [
    path('enroll/', views.EnrollView.as_view(), name = 'enroll'),
    #path('register/', views.RegisterView.as_view(), name = 'register'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('user/<pk>', views.UserView.as_view(), name='user'),
    path('changepassword/', views.ChangePasswordView.as_view(), name='change_password'),
]
