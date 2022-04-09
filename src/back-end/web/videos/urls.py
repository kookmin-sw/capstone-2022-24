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
from videos.views import HomeView

urlpatterns = [
    path('/videos',HomeView.as_view(), name ='home'), #/videos?search=__title__or__cast&page=___&size=____
    path('/videos/movie/<int:pk>', views.MovieDetails, name= 'movieDetail'), #/videos/movie/{video_id}
    path('/videos/tv/<int:pk>', views.TVDetails, name= 'tvDetail'), #/videos/tv/{video_id} 이거...는 리다이랙트 하는건데 어케 처리할지는 알아봐야겠삼
    path('/videos/tv/<int:pk>/season/<int:num>', views.TVDetails, name= 'tvDetail'), #/videos/tv/{video_id}/season/{season_num}
    path('/vidoes/movie/<int:pk>/casts', views.castsDetails, name="movieCast"), #/videos/movie/{video_id}/casts
]
