from django.shortcuts import render

# Create your views here.
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
