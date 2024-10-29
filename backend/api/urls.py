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
    path('yarns', yarns_api_view, name='yarns'),
    path('patterns', patterns_api_view, name='patterns'),
    path('users', users_api_view, name='users'),
    path('projects', projects_api_view, name='projects'),
    path('patternyarns', patternyarns_api_view, name='patternyarns')
 ]
