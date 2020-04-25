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

"""edit this to match projectname"""
from . import settings



""""the paths for the login and logout are done using the built-in django features"""


urlpatterns = [
    path('admin/', admin.site.urls, name='admin-login'),
    path('', views.landing, name='landing'),
    path('question/', views.question_detail, name='question_detail'),
    path('question/custom/', views.question_customize, name='question_customize'),
    path('question/reroll/', views.question_customize_reroll, name='question_customize_reroll'),
    path('report-error/', views.report_error, name='report_error'),


    # path('login/', auth_views.LoginView.as_view(),{'template_name':'registration/login.html'},name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), {'next_page':''}, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
