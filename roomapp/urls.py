from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('checkin/', views.dashboard, name='checkin'),
    path('checkout/', views.dashboard, name='checkout'),
    path('addroom/', views.dashboard, name='addroom'),
    path('reserveroom/', views.dashboard, name='reserveroom'),
    path('roommanager/', views.dashboard, name='roommanager'),  
   
]