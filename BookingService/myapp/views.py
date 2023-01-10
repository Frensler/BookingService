from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages

from .models import Room, Client, Reservation
from .forms import RoomForm, ClientForm, ReservationForm

def index(request):
    return render(request,"myapp/base.html")

#Rooms part start
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

def checkIn(request, roomId):
    if request.method == "POST":
        formReservation = ReservationForm(request.POST)
        if formReservation.is_valid():
            dateFrom=formReservation.cleaned_data.get("dateFrom")
            dateTo=formReservation.cleaned_data.get("dataTo")
            if ( dateFrom == datetime.date.today() and dateTo > datetime.date.today()):
                room = get_object_or_404(Room,id=roomId)     
                reservation = Reservation(dateFrom=dateFrom,dataTo=dateTo,client=formReservation.cleaned_data.get("client"),room=room)
                reservation.save()
                room.occupied = True
                room.save()
                return HttpResponseRedirect(reverse('rooms'))
            else:
                messages.error(request, 'Form is not valid!')
                room = get_object_or_404(Room,id=roomId)
                formReservation = ReservationForm()
                return render(request,"myapp/roomCheckIn.html", {'room':room, 'formReservation': formReservation})

        else:
            messages.error(request, 'Form is not valid!')
            room = get_object_or_404(Room,id=roomId)
            formReservation = ReservationForm()
            return render(request,"myapp/roomCheckIn.html", {'room':room, 'formReservation': formReservation})
    else:
        room = get_object_or_404(Room,id=roomId)
        formReservation = ReservationForm()
        return render(request,"myapp/roomCheckIn.html", {'room':room, 'formReservation': formReservation})

def checkOut(request, roomId):
    if request.method == "POST":
        room = Room.objects.get(id=roomId)
        room.occupied = False
        room.save()
    return HttpResponseRedirect(reverse('rooms'))

def addNewRoom_index(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rooms'))
    else:    
        form = RoomForm()
        return render(request,"myapp/addNewRoom.html", {'form': form})
#Rooms part end


def reservations_index(request):
    context = { "reservations": Reservation.objects.all()}
    return render(request,"myapp/reservations.html",context)

def clients_index(request):
    context = { "clients": Client.objects.all()}
    return render(request,"myapp/clients.html",context)

def addOrEditClient_index(request,clientId=None):
    if clientId:
        client = get_object_or_404(Client, pk=clientId)
    else:
        client = Client()
    form = ClientForm(request.POST or None, instance=client)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('clients'))
    return render(request,"myapp/addOrEditClient.html", {'clientId': clientId or None, 'form': form})

def deleteClient(request, clientId):
    if request.method == "POST":
        room = Client.objects.get(id=clientId)
        room.delete()
    return HttpResponseRedirect(reverse('clients'))