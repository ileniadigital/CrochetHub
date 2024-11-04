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

# CHANGE URLS SO THAT WHEN IT'S UPDATE AND DELETE IT CALLS A FUNCTION THAT CHECKS IF THE METHOD IS UPDATE OR DELETE
# NEED TO REMOVE THE /update stuff

urlpatterns = [
    # API entry points should be defined here
    path('yarn', yarn_api_view, name='yarn'),
    path('yarn/<int:id>/update/', yarn_put, name='yarnUpdate'),
    path('yarn/<int:id>/delete/', yarn_delete, name='yarnDelete'),
    path('pattern', pattern_api_view, name='pattern'),
    path('pattern/<int:id>/update/', pattern_put, name='patternUpdate'),
    path('pattern/<int:id>/delete/', pattern_delete, name='patternDelete'),
    path('user', user_api_view, name='user'),
    path('user/<int:id>/update/', user_put, name='userUpdate'),
    path('user/<int:id>/delete/', user_delete, name='userDelete'),
    path('project', project_api_view, name='project'),
    path('project/<int:id>/update/', project_put, name='projectUpdate'),
    path('project/<int:id>/delete/', project_delete, name='projectDelete'),
    path('patternyarn/', patternyarn_api_view, name='patternyarn'),
    path('patternyarn/<int:id>/update/', patternyarn_put, name='patternyarnUpdate'),
    path('patternyarn/<int:id>/delete/', patternyarn_delete, name='patternyarnDelete'),
]
