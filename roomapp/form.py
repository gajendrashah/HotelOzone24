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

class BookingUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Booked
        fields = "__all__"
        # exclude = ["customer_details","room_id","child","male_number","female_number","other_gender"]