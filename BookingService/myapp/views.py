from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages

from .models import Room, Client, Reservation
from .forms import RoomForm, ClientForm, ReservationForm

def index(request):
    return render(request,"myapp/base.html")

def rooms_index(request):
    context = { "rooms": Room.objects.all()} #context, ktory przekazemy do widoku
    return render(request,"myapp/rooms.html",context)

def roomDetails_index(request,roomId):
    # try:
    #     room = Room.objects.get(number=room_no)
    # except:
    #     raise Http404("Room not found!")
    room = get_object_or_404(Room,id=roomId)
    return render(request,"myapp/roomDetails.html", {"room":room})

def checkOut(request, roomId):
    if request.method == "POST":
        room = Room.objects.get(id=roomId)
        room.occupied = False
        room.save()
    return HttpResponseRedirect(reverse('rooms'))
    
def reservations_index(request):
    context = { "reservations": Reservation.objects.all()}
    return render(request,"myapp/reservations.html",context)

def clients_index(request):
    context = { "clients": Client.objects.all()}
    return render(request,"myapp/clients.html",context)