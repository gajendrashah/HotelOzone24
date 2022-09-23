from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('checkin/', views.checkin, name='checkin'),
    path('checkout/', views.checkout, name='checkout'),
    path('addroom/', views.addroom, name='addroom'),
    path('reserveroom/', views.reserveroom, name='reserveroom'),
    path('reservation_edit/<int:pk>/', views.reservation_edit, name='reservation_edit'),
    path('roommanager/', views.roommanager, name='roommanager'),
    path('report/', views.customerdetail, name='report'),
    path('signin/', views.user_login, name='signin'),  
    path('signup/', views.user_signup, name='signup'),  
    path('logout/', views.user_logout, name='logout'),  
    path('with_room/', views.with_room, name='withroom'),  
    path('resturant/with_out_room/', views.with_out_room, name='withoutroom'),  

   
]