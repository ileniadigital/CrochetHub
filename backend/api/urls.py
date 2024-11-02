"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
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
from django.urls import path
from .views import *


urlpatterns = [
    # API entry points should be defined here
    path('yarn', yarn_api_view, name='yarn'),
    path('yarn/<int:id>', yarn_put, name='yarnChange'),
    path('pattern', pattern_api_view, name='pattern'),
    path('pattern/<int:id>', pattern_put, name='patternChange'),
    path('user', user_api_view, name='user'),
    path('user/<int:id>', user_put, name='userChange'),
    path('project', project_api_view, name='project'),
    path('project/<int:id>', project_put, name='projectChange'),
    path('patternyarn', patternyarn_api_view, name='patternyarn'),
    path('patternyarn/<int:id>', patternyarn_put, name='patternyarnChange'),
 ]
