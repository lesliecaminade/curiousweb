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

"""edit this to match projectname
optionally, using a "." makes the import at the same directory as this file is"""
from . import settings


urlpatterns = [
    path('controlcenter/', admin.site.urls, name='admin-login'),
    path('', views.IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    #i am starting to decide to migrate some of my work to class based view so here it is
    path('main_app/', include('main_app.urls', namespace='main_app')),
    path('studentsece_app/', include('studentsece_app.urls', namespace='studentsece_app')),
    path('studentsee_app/', include('studentsee_app.urls', namespace='studentsee_app')),
    path('studentstutorial_app/', include('studentstutorial_app.urls', namespace='studentstutorial_app')),
    path('exams_app/',include('exams_app.urls', namespace='exams_app')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
