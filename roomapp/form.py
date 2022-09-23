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