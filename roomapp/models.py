from django.db import models
import random
import string
from datetime import date, datetime,timedelta





def random_string_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_user_generator(size=3, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
# Create your models here.

class Customer(models.Model):
    full_name = models.CharField(max_length=255,blank=True)
    user = models.CharField(max_length=255,default = (f'#{random_string_generator()}').upper(),unique=False)    
    organization = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(max_length=255,null=True,blank=True)
    designation = models.CharField(max_length=255,blank=True)
    passport_id_number = models.CharField(max_length=255,blank=True)
    location = models.CharField(max_length=255,blank=True)
    phone_number = models.IntegerField(blank=True, help_text='Contact phone number')
    nationality = models.CharField(max_length=155,blank=True)
    tel_fax = models.CharField(max_length=255,blank=True)
    traval_agent = models.CharField(max_length=255,blank=True)
    bill_setteled_by = models.CharField(max_length=255,blank=True)
    booked_by = models.CharField(max_length=255,blank=True)
    check_in = models.DateTimeField(auto_now=False,null=True)
    check_out = models.DateTimeField(auto_now=False,null=True)
    main_id = models.ImageField(upload_to="customer/id",null=True)



  
    
    def format_date(obj):
        return obj.check_in.strftime('%d %b %Y %H:%M')
    
    



    def __str__(self):
        return self.full_name

class Grouped_room(models.Model):
    title = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.title



class Room(models.Model):
    room_status = (
        ("available", "available"),
        ("booked","booked"),
        ("not-confirm","confirm"),
        ("cancled","cancled"),
        ("cleaning", "cleaning"),
        ("maintainance", "maintainance"),)
    room_number = models.CharField(max_length=255)
    group = models.ForeignKey(Grouped_room,on_delete=models.CASCADE,blank=True)
    price_pernight = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=room_status, default="available")
    intital_number = models.IntegerField(default=0)
    final_number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.room_number}"


class Booked(models.Model):
    customer_details = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    room_id = models.ManyToManyField(Room, blank=True)
    number_of_days = models.IntegerField(default=0)
    booked_date = models.DateTimeField(auto_now_add=True,null=True)
    child = models.IntegerField(default=0,null=True)
    male_number = models.IntegerField(default=0,null=True)
    female_number = models.IntegerField(default=0,null=True)
    other_gender = models.IntegerField(default=0,null=True)
    status = models.BooleanField(default=False)
    class Meta:
        ordering =["-booked_date"]
        
    @property
    def total_room(self):
        total_room = self.room_id.objects.all()
        return total_room

    def __str__(self):
        return f'{self.customer_details}'

    @property
    def business_days(self):
        holidays = Customer.objects.values_list('check_in', flat=True)
        oneday = timedelta(days=1)
        # print(oneday)
        dt = self.booked_date.date()
        # print("this is dt",dt)
        total_days = 0
        while (dt <= date.today()):
            if not dt.isoweekday() in (6, 7) and dt not in holidays.values():
                total_days += 1
            dt += oneday
        return total_days