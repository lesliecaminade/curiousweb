from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'handouts'

urlpatterns = [
    path('', views.Handouts.as_view(), name = 'main'),
    path('add/', views.AddHandout.as_view(), name='add'),
    path('addfile/<handoutpk>', views.AddHandoutFile.as_view(), name='addhandoutfile'),
    path('download/<filepk>', views.DownloadHandoutFile.as_view(), name='download'),
    path('detail/<handoutpk>', views.HandoutDetail.as_view(), name='detail'),
    path('delete/<handoutpk>', views.HandoutDelete.as_view(), name='delete'),
    path('lock/<handoutpk>', views.HandoutLock.as_view(), name='handout_lock'),
    path('unlock/<handoutpk>', views.HandoutUnlock.as_view(), name='handout_unlock'),
    path('toggle/<pk>/<flag>/<setting>', views.ToggleFlag.as_view(), name='toggle_flag'),
]
