from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('checkin/', views.checkin, name='checkin'),
    path('checkout/', views.checkout, name='checkout'),
    path('addroom/', views.addroom, name='addroom'),
    path('reserveroom/', views.reserveroom, name='reserveroom'),
    path('roommanager/', views.roommanager, name='roommanager'),
    path('report/', views.customerdetail, name='report'),
   
]