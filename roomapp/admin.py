from django.contrib import admin

from roomapp.models import Booked, Customer, Customer_list, Room

# Register your models here.
admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(Booked)
admin.site.register(Customer_list)