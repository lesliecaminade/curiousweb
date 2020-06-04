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
    path('users_filter/<filter>', views.UserListFilterView.as_view(), name='users_filter'),
    path('deactivate/<userpk>', views.DeactivateUser.as_view(), name='deactivate'),
    path('activate/<userpk>', views.ActivateUser.as_view(), name='activate'),
    path('createannouncement/', views.CreateAnnouncement.as_view(), name='create_announcement'),
    path('deleteannouncement/<announcementpk>', views.DeleteAnnouncement.as_view(), name='delete_announcement'),

]
