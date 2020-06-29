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
from main_app import views as views
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
"""edit this to match projectname
optionally, using a "." makes the import at the same directory as this file is"""
from . import settings


urlpatterns = [
    path('controlcenter/', admin.site.urls, name='admin-login'),
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/<activetab>', views.IndexView.as_view(), name='index'),
    path('login/', csrf_exempt(auth_views.LoginView.as_view(template_name="login.html")),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    #i am starting to decide to migrate some of my work to class based view so here it is
    path('main_app/', include('main_app.urls', namespace='main_app')),
    path('students_app_1/', include('students_app_1.urls', namespace='students_app_1')),
    path('students_app_2/', include('students_app_2.urls', namespace='students_app_2')),
    path('students_app_3/', include('students_app_3.urls', namespace='students_app_3')),
    path('exams_app/',include('exams_app.urls', namespace='exams_app')),
    path('staticpages/', include('staticpages.urls', namespace='staticpages')),
    path('handouts/', include('handouts.urls', namespace='handouts')),
    path('exams_app_2/',include('exams_app_2.urls', namespace='exams_app_2')),
    path('exams_app_3/',include('exams_app_3.urls', namespace='exams_app_3')),
    path('testimonials/', include('testimonials.urls', namespace = 'testimonials')),
    path('downloadables/', include('downloadables.urls', namespace = 'downloadables')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
