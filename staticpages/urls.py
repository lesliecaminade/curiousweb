from django.urls import path
from . import views


app_name = 'staticpages'

urlpatterns = [
    path('staticpages/ece', views.ScheduleECE.as_view(), name='calendar_ece'),
    path('staticpages/ee', views.ScheduleEE.as_view(), name='calendar_ee'),
    path('staticpages/location', views.Location.as_view(), name='location'),
    path('staticpages/reviewers', views.Reviewers.as_view(), name='reviewers'),

]
