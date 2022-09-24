from django import forms
from .models import *
class RoomCreationForm(forms.Form):
    initial_number = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control mt-2"}))
    final_number  = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control mt-2"}))
    room_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mt-2"}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control mt-2"}))


class ReservationCreationForm(forms.ModelForm):
    room = forms.ModelMultipleChoiceField(queryset=Room.objects.filter(status="available"))
    Child = forms.CharField( widget=forms.NumberInput(attrs={"class":"form-control mt-2"}),)
    male_number = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"form-control mt-2"}),)
    female_number = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"form-control mt-2"}),)
    Other_gender = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"form-control mt-2"}),)
    number_of_days = forms.IntegerField( widget=forms.NumberInput(attrs={"class":"form-control mt-2"}),)
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ["qr_code","user","check_out"]
        widgets ={
        "full_name" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "email" : forms.EmailInput(attrs={"class":"form-control mt-2"}),
        "organization" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "designation" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "passport_id_number" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "phone_number" : forms.NumberInput(attrs={"class":"form-control mt-2"}),
        "tel_fax" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "traval_agent" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "nationality" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "location" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "bill_setteled_by" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "booked_by" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "room" : forms.SelectMultiple(attrs={"class":"form-control mt-2"}),
        "main_id" : forms.FileInput(attrs={"class":"form-control "}),
        "check_in" : forms.DateInput(attrs={"class":"form-control",}),
 
        }

class CustomerCretionForm(forms.ModelForm):
    
    # room = forms.ModelMultipleChoiceField(queryset=Room.objects.filter(status="available"))
    main_additional_id = forms.FileField( widget=forms.FileInput(attrs={"class":"form-control mt-2",'multiple': True}))

    Child = forms.CharField( widget=forms.TextInput(attrs={"class":"form-control mt-2"}),)
    male_number = forms.IntegerField( widget=forms.TextInput(attrs={"class":"form-control mt-2"}),)
    female_number = forms.IntegerField( widget=forms.TextInput(attrs={"class":"form-control mt-2"}),)
    Other_gender = forms.IntegerField( widget=forms.TextInput(attrs={"class":"form-control mt-2"}),)
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ["qr_code","check_in","check_out"]
        widgets ={
        "full_name" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "user" : forms.HiddenInput(attrs={"class":"form-control mt-2"}),
        "email" : forms.EmailInput(attrs={"class":"form-control mt-2"}),
        "organization" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "designation" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "passport_id_number" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "phone_number" : forms.NumberInput(attrs={"class":"form-control mt-2"}),
        "tel_fax" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "traval_agent" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "nationality" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "location" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "bill_setteled_by" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "booked_by" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "room" : forms.SelectMultiple(attrs={"class":"form-control mt-2"}),
        "main_id" : forms.FileInput(attrs={"class":"form-control "}),
        "main_additional_id" : forms.ClearableFileInput(attrs={"class":"form-control input-group-prepend",'multiple': True}),
        
 
        }


class Advance_paymentForm(forms.Form):
    Payment_type = (
        ("Esewa", "Eswa"),
        ("Khalti", "Khalti"),
        ("Bank Transfer", "Bank Transfer"),
        ("Cash", "Cash"),
        ("Other", "Other"),
        )
    Advance_amount =forms.IntegerField( required=True,widget=forms.NumberInput(attrs={"class":"form-control form-white"}))
    payment_type =forms.ChoiceField(choices=Payment_type, required=True,widget=forms.Select(attrs={"class":"form-control form-white"}))
    remarks =forms.CharField(max_length=255, required=True,widget=forms.TextInput(attrs={"class":"form-control form-white"}))

class BookedAccountupdateForm(forms.ModelForm):
    class Meta:
        model= Booked
        fields="__all__"
        exclude = ["status","customer_details","number_of_days"]


class CustomerCretionForm1(forms.ModelForm):
    
   
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ["check_out"]
        widgets ={
        "full_name" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "user" : forms.HiddenInput(attrs={"class":"form-control mt-2"}),
        "email" : forms.EmailInput(attrs={"class":"form-control mt-2"}),
        "organization" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "designation" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "passport_id_number" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "phone_number" : forms.NumberInput(attrs={"class":"form-control mt-2"}),
        "tel_fax" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "traval_agent" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "nationality" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "location" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "bill_setteled_by" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "booked_by" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "room" : forms.SelectMultiple(attrs={"class":"form-control mt-2"}),
        "main_id" : forms.FileInput(attrs={"class":"form-control "}),
        "main_additional_id" : forms.ClearableFileInput(attrs={"class":"form-control input-group-prepend",'multiple': True}),
        
 
        }



class OrderCreationForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=Room.objects.filter(status="booked"))
    class Meta:
        model = Order
        fields = '__all__'
        exclude =["id","customer","order_status","payment_type"]
        
        widgets ={
            "order_id" : forms.TextInput(attrs={"class":"form-control"}),
            "room" : forms.Select(attrs={}),
            "total" : forms.NumberInput(attrs={"class":"form-control"}),
        }

class Order_creation_Non_room_user(forms.ModelForm):
    class Meta:
        model = Non_room_user
        fields = "__all__"
        widgets ={
        "full_name" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "order_id" : forms.TextInput(attrs={"class":"form-control mt-2"}),
        "phone_number" : forms.NumberInput(attrs={"class":"form-control mt-2"}),
        "email" : forms.EmailInput(attrs={"class":"form-control mt-2"}),
        "total" : forms.NumberInput(attrs={"class":"form-control mt-2"}),
        "payment_type" : forms.Select(attrs={"class":"form-control mt-2"}),
        
 
        }

class Non_room_OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Non_room_user
        fields = '__all__'
        exclude =["id","customer","order_status"]
        
        widgets ={
            "order_id" : forms.TextInput(attrs={"class":"form-control"}),
            "phone_number" : forms.TextInput(attrs={"class":"form-control"}),
            "email" : forms.EmailInput(attrs={"class":"form-control"}),
            "full_name" : forms.TextInput(attrs={"class":"form-control"}),
            
            "total" : forms.NumberInput(attrs={"class":"form-control"}),
            "order_status" : forms.Select(attrs={"class":"form-control"}),
            "payment_type" : forms.Select(attrs={"class":"form-control"}),
        }