from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('checkin/', views.dashboard, name='checkin'),
    path('checkout/', views.dashboard, name='checkout'),
    path('addroom/', views.dashboard, name='addroom'),
    path('reserveroom/', views.dashboard, name='reserveroom'),
    path('roommanager/', views.dashboard, name='roommanager'),  
    path('signin/', views.user_login, name='signin'),  
    path('signup/', views.user_signup, name='signup'),  
    path('logout/', views.user_logout, name='logout'),  

   
]