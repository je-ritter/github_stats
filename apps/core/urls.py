from django.urls import path

from apps.core import views



urlpatterns = [
    path('', views.home, name='home'),
    path('allrepos/', views.allrepos, name='allrepos'),
    path('visualrepos/', views.visualrepos, name='visualrepos'),
    path('viewpanels/', views.viewpanels, name='viewpanels'),
    path('details/<panel_id>/', views.panel_details,),
    path('user-dashboards/<the_username>/', views.view_user_dash),
	]

