from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'downloadables'

urlpatterns = [
    path('', views.Downloadables.as_view(), name = 'main'),
    path('add/', views.AddDownloadable.as_view(), name='add'),
    path('addfile/<downloadablepk>', views.AddDownloadableFile.as_view(), name='adddownloadablefile'),
    path('download/<filepk>', views.DownloadDownloadableFile.as_view(), name='download'),
    path('detail/<downloadablepk>', views.DownloadableDetail.as_view(), name='detail'),
    path('delete/<downloadablepk>', views.DownloadableDelete.as_view(), name='delete'),
    path('lock/<downloadablepk>', views.DownloadableLock.as_view(), name='downloadable_lock'),
    path('unlock/<downloadablepk>', views.DownloadableUnlock.as_view(), name='downloadable_unlock'),
    path('toggle/<pk>/<flag>/<setting>', views.ToggleFlag.as_view(), name='toggle_flag'),
]
