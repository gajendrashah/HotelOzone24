import datetime
from django.http import JsonResponse,Http404
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required, permission_required

from roomapp.form import BookingUpdateForm, ReservationCreationForm, RoomCreationForm
from roomapp.models import Booked, Customer, Grouped_room, Room

# Create your views here.
@login_required(login_url="signin")
def dashboard(request):
    return render(request, 'index.html')

@login_required(login_url="signin")
def checkin(request):
    return render(request, 'roomapp/checkin.html')

@login_required(login_url="signin")
def checkout(request):

    return render(request, 'roomapp/checkout.html')

@login_required(login_url="signin")
def addroom(request):
    form = RoomCreationForm
    rooms= Room.objects.all()
    if request.method == "POST":

        form = RoomCreationForm(request.POST)
        if form.is_valid():
            first_number = form.cleaned_data.get("initial_number")
            last_number = form.cleaned_data.get("final_number")
            
            room_group = form.cleaned_data.get("room_name")
            price = form.cleaned_data.get("price")
            room_list = list(range(first_number,last_number+1))
            obj = Grouped_room.objects.create(title=room_group)
            # obj.save(commit=False)
            obj.save()
            group_id = Grouped_room.objects.get(id=obj.id)

            for data in room_list:
                obj = Room.objects.create(group= group_id,room_number=data,price_pernight=price,intital_number=first_number,final_number=last_number)
                obj.save()
            messages.success(request,"Room are Createted !!!")
            return redirect("addroom")
        else:
            messages.error(request,"Room Cant Create !!")
            return redirect("roomdetails")




    context = {"allrooms":rooms,"form":form}

    return render(request, 'roomapp/addroom.html',context)

@login_required(login_url="signin")
def reserveroom(request):
    cs = Booked.objects.filter(status= False)
    form = ReservationCreationForm

    av_room = Room.objects.filter(status="available")
   
    if request.method == "POST":
        # print(request.POST,request.FILES)
        form =ReservationCreationForm(request.POST,request.FILES)
        room_id = request.POST.getlist("room")
        if form.is_valid():
            data = form.save(commit=False)
           
            form.save()
            child = form.cleaned_data.get("Child")
            male_number = form.cleaned_data.get("male_number")
            female_number = form.cleaned_data.get("female_number")
            other_gender = form.cleaned_data.get("Other_gender")
            number_of_days = form.cleaned_data.get("number_of_days")
            user = Customer.objects.get(id=data.pk)

            res = [eval(i)for i in room_id]
            book_id = Booked.objects.create(customer_details=user,number_of_days=number_of_days, child=child,male_number=male_number,female_number=female_number,other_gender=other_gender)
            book_id.room_id.set(res)
            book_id.save()


            for rid in room_id:
                room_update = Room.objects.get(id=rid)
                room_update.status= "not-confirm"
                room_update.save()
            messages.success(request,"Your Resevation is complete")
            return redirect("reserveroom")
        else:
            messages.error(request,form.errors)
            return redirect("reserveroom")
    context = {"customers": cs, "av_room": av_room, "form":form}
    return render(request, 'roomapp/reserve_room.html',context)


def reservation_edit(request,pk):
    foo_ = Booked.objects.get(id=pk)
    cus = Customer.objects.get(id = foo_.customer_details_id)
    print("foo",foo_)
    form = ReservationCreationForm(instance=cus)
    room_id = request.POST.getlist("room")
    if request.method == "POST":
        form = ReservationCreationForm(request.POST,request.FILES,instance=cus)
        if form.is_valid():
            data= form.save(commit=False)

            child = form.cleaned_data.get("Child")
            print("Child",child)
            male_number = form.cleaned_data.get("male_number")
            female_number = form.cleaned_data.get("female_number")
            other_gender = form.cleaned_data.get("Other_gender")
            number_of_days = form.cleaned_data.get("number_of_days")

            Bks = Booked.objects.get(customer_details_id=data.pk)
            Bks.child= child
            Bks.male_number = male_number
            Bks.female_number = female_number
            Bks.other_gender = other_gender
            Bks.number_of_days = number_of_days
            
            
            
            res = [eval(i)for i in room_id]
            Bks.room_id.set(res)
            Bks.save()

            for rid in room_id:
                room_update = Room.objects.get(id=rid)
                room_update.status= "not-confirm"
                room_update.save()

            
            form.save()
            messages.success(request,"Data updated successfully !!!")
            return redirect("reserveroom")



    context={"form":form}
    return render(request,"roomapp/reserve_room_edit.html",context)
 

@login_required(login_url="signin")
def roommanager(request):

    return render(request, 'roomapp/room_manager.html')

def customerdetail(request):
    return render(request, 'roomapp/room_manager.html')

def with_room(request):
    return render(request,"resturentapp/withroom.html")


def with_out_room(request):
    return render (request,"resturentapp/withoutroom.html")

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

    return render(request,"extra pages/signin.html")


def user_signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':  
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']  

            print("here we are")
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already taken')
                    return redirect('signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already taken')
                    return redirect('signup')    
                else:    
                    user = User.objects.create_user(username=username, email=email,password=password1)
                    user.save()
                    return redirect('signin')
            else:
                messages.info(request,'Password did not matched.')
                return redirect('signup')
        

    return render(request,"extra pages/signup.html")


def user_logout(request):
    auth.logout(request)
    return redirect('signin')


def edit_room(request):
    form = RoomCreationForm
    if request.method == "POST":

        form = RoomCreationForm(request.POST)
        if form.is_valid():
            first_number = form.cleaned_data.get("initial_number")
            last_number = form.cleaned_data.get("final_number")
            
            room_group = form.cleaned_data.get("room_name")
            price = form.cleaned_data.get("price")

            
            r = Room.objects.filter(intital_number=first_number,final_number=last_number)
            r.delete()
            g = Grouped_room.objects.filter(title=room_group)
            g.delete()


            room_list = list(range(first_number,last_number+1))
            obj = Grouped_room.objects.create(title=room_group)
            # obj.save(commit=False)
            obj.save()
            group_id = Grouped_room.objects.get(id=obj.id)

            for data in room_list:
                obj = Room.objects.create(group= group_id,room_number=data,price_pernight=price,intital_number=first_number,final_number=last_number)
                obj.save()
            messages.success(request,"Room are Createted !!!")
            return redirect("addroom")
        else:
            messages.error(request,"Room Cant Create !!")
            return redirect("roomdetails")


    context ={"form":form}
    return render(request,"update_room.html",context)