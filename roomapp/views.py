from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User , auth

# Create your views here.
# @login_required("signup")
def dashboard(request):
    return render(request, 'index.html')

def checkin(request):
    return render(request, 'checkin.html')

def checkout(request):
    return render(request, 'checkout.html')

def addroom(request):
    return render(request, 'addroom.html')

def reserveroom(request):
    return render(request, 'reserve_room.html')

def roommanager(request):
    return render(request, 'room_manager.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

    return render(request,"pages/signin.html")


def user_signup(request):
    print(request.POST)
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
        

    return render(request,"pages/signup.html")


def user_logout(request):
    auth.logout(request)
    return redirect('signin')
    