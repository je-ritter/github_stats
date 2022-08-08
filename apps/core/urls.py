from django.urls import path

from apps.core import views



urlpatterns = [
    path('', views.home, name='home'),
    path('allrepos/', views.allrepos, name='allrepos'),
    path('visualrepos/', views.visualrepos, name='visualrepos'),
]

