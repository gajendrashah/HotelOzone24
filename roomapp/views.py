from datetime import date
import json
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.http import Http404,JsonResponse
from roomapp.form import BookedAccountupdateForm, CustomerCretionForm, CustomerCretionForm1, ReservationCreationForm, RoomCreationForm
from roomapp.models import Additional_id, Booked, Customer, Customer_list, Grouped_room, Room

# Create your views here.
@login_required(login_url="signin")
def dashboard(request):
    return render(request, 'index.html')
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def get_room_by_group(request):
    grouped_room = Grouped_room.objects.all().values()
    return JsonResponse(list(grouped_room),safe=False)

@login_required(login_url="signin")
def checkin(request):
    form = CustomerCretionForm
    customer_list = Customer_list.objects.filter(status=True)
    if request.method == "POST":
        rooms = request.POST.getlist("id_room")
        main_id_add= request.FILES.getlist("main_additional_id")

        if rooms != []:
            user_id = request.POST.get("user")
            try:
                users = Customer.objects.get(user=user_id)
                if users:
                    form = CustomerCretionForm(request.POST,request.FILES,instance=users)
                else:
                    form = CustomerCretionForm(request.POST,request.FILES)
            except:
                form = CustomerCretionForm(request.POST,request.FILES)
            
            if form.is_valid:
                data = form.save(commit=False)
                data.check_in = date.today()
                form.save()
                # print(form.pk)
                child = form.cleaned_data.get("Child")
                male_number = form.cleaned_data.get("male_number")
                female_number = form.cleaned_data.get("female_number")
                other_gender = form.cleaned_data.get("other_gender")
                print("here is a id ",main_id_add)
                user = Customer.objects.get(id = data.pk)
                
                for img in main_id_add:
                    obs = Additional_id.objects.create(customer=user,add_id=img)
                    obs.save()
                # print(main_id_add)            
            
                res = [eval(i) for i in rooms]
                get_room_list = Room.objects.filter(id__in=rooms)
        
                book_id = Booked.objects.create(customer_details=user, child=child,male_number=male_number,female_number=female_number,other_gender=other_gender)
                book_id.room_id.set(res)
                book_id.status=True
                book_id.save()
                x = Booked.objects.get(id=book_id.pk)
                cus_active = Customer_list.objects.create(customer=user,bookd_roooms=x)
                cus_active.save()
                for room in get_room_list:
                    room.status ="booked"
                    room.save()
                messages.success(request, 'Customer creation successfully ')
                return redirect("checkin")
        else:
            messages.error(request, 'Please Provide room data')
            return redirect("checkin")
    
    if is_ajax(request=request):
        term = request.GET.get("room")
        group = Grouped_room.objects.get(title=term)
        room = Room.objects.filter(status="available",group=group).values()
        # print(room)
        return JsonResponse(list(room),safe=False)

    context={"customer_list":customer_list,"form":form}
    return render(request, 'roomapp/checkin.html',context)

def checkin_edit(request,pk):
    cus = Customer.objects.get(id=pk)
    b = Booked.objects.get(customer_details=cus)
    print(b)
    customer_form = CustomerCretionForm1(instance=cus)
    book_form = BookedAccountupdateForm(instance=b)
    if request.method=="POST":
        customer_form = CustomerCretionForm1(request.POST,request.FILES,instance=cus)
        book_form = BookedAccountupdateForm(request.POST,request.FILES,instance=b)
        if customer_form.is_valid():
            customer_form.save()
        if book_form.is_valid():
            book_form.save()
        return redirect("checkin")

    context={"customer_form":customer_form,"book_form":book_form}
    return render(request,"roomapp/check_in_edit.html",context)

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
 

def reservation_checkin(request):
    if request.method != "POST":
        raise Http404
    
    else:
        print(request.POST)
        booke_id = request.POST.get("bookd_id")
        books_= Booked.objects.get(id=booke_id)
        print(books_)
        books_.status = True
        cus= cus = Customer_list.objects.create(bookd_roooms=books_,customer=books_.customer_details)
        cus.status=True
        for r in books_.room_id.all():
            r.status = "booked"
            r.save()
        cus.save()
        books_.save()

        return JsonResponse({"msg":"This is working "},safe=False)

def reservation_cancle(request,pk):
    booked = get_object_or_404(Booked,id=pk)
    for r in booked.room_id.all():
        r.status = "available"
        r.save()
        booked.delete()
        messages.success(request,"Booking cancle sucssfully !!!")
    return redirect("reserveroom")



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