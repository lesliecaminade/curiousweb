"""curiousweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from main_app import views
from django.conf.urls.static import static

"""edit this to match projectname
optionally, using a "." makes the import at the same directory as this file is"""
from . import settings


urlpatterns = [
    path('controlcenter/', admin.site.urls, name='admin-login'),
    path('', views.landing, name='home'),
    path('', views.landing, name='landing'),
    path('question/custom/', views.question_customize, name='question_customize'),
    path('question/reroll/', views.question_customize, name='question_customize_reroll'),
    path('report-error/', views.report_error, name='report_error'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('enroll/',views.enroll, name='enroll'),
    path('enroll/ece/<first_name>/<last_name>/<middle_name>',views.enroll_ece, name='enroll_ece'),
    path('enroll/ee/<first_name>/<last_name>/<middle_name>',views.enroll_ee, name='enroll_ee'),
    path('enroll/tutorial/<first_name>/<last_name>/<middle_name>',views.enroll_tutorial, name='enroll_tutorial'),
    path('mcq/create', views.create_multiple_choice_question, name='create_multiple_choice_question'),
    path('mcq/customize/', views.multiple_choice_question_customize, name='multiple_choice_question_customize'),
    path('mcq/detail', views.multiple_choice_question_customize, name='multiple_choice_detail'),
    path('mcq/detail/<pk>', views.multiple_choice_question_specific, name='multiple_choice_detail_specific'),
    path('mcq/list/', views.multiple_choice_question_list, name='multiple_choice_question_list'),
    path('mcq/list/select', views.multiple_choice_question_list, name='multiple_choice_question_list_select'),
    path('mcq/delete/<pk>', views.multiple_choice_question_delete, name='multiple_choice_question_delete'),
    path('load_subtopics/ajax/', views.load_subtopics, name='ajax_load_subtopics'),
    path('mcq/exam/', views.exam_configure, name='exam_configure'),
    path('mcq/exam/results/', views.exam_results, name='exam_results'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
