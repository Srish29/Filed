"""filed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # views/index.py
    path('', views.home, name='home'),
    path('create/audio', views.create_audio, name='create_audio'),
    path('delete/audio/<str:type>/<str:id>', views.delete_audio, name='delete_audio'),
    path('update/audio/<str:type>/<str:id>', views.update_audio, name='update_audio'),
    path('get/audio/<str:type>/<str:id>', views.get_audio, name='get_audio'),
    path('get/audio/<str:type>', views.get_all_audio, name='get_all_audio'),
]

