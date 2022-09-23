from django.contrib import admin

from roomapp.models import Booked, Customer, Room

# Register your models here.
admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(Booked)