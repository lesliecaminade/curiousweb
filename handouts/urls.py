from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'handouts'

urlpatterns = [
    path('', views.Handouts.as_view(), name = 'main'),
    path('add/', views.AddHandout.as_view(), name='add'),
    path('download/<handout>', views.DownloadHandout.as_view(), name='download'),


]
