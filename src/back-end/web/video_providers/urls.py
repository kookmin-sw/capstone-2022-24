"""videos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from video_providers import views

urlpatterns =[
    path('/discontinues/7days',views.providersList(), name ='7days'), #/discontinues/7days
    path('/discontinues/15days',views.providersList(), name ='15days'), #/discontinues/15days
    path('/discontinues/30days',views.providersList(), name ='30days'), #/discontinues/30days
]