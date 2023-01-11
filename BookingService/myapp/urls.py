from django.urls import path
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('rooms/', views.rooms_index, name='rooms'),
    path('rooms/<int:roomId>', views.roomDetails_index, name='roomDetails'),
    path('rooms/addNewRoom', views.addNewRoom_index, name='addNewRoom'),
    path('rooms/<int:roomId>/checkOut', views.checkOut, name='checkOut'),
    path('rooms/<int:roomId>/checkIn', views.checkIn, name='checkIn'),
    path('reservations/', views.reservations_index, name='reservations'),
    path('clients/', views.clients_index, name='clients'),
    path('clients/edit/<int:clientId>', views.addOrEditClient_index, name='editClient'),
    path('clients/new', views.addOrEditClient_index, name='newClient'),
    path('clients/delete/<int:clientId>', views.deleteClient, name='deleteClient'),
    path('reservations/edit/<int:reservationId>', views.editReservation_index, name='editReservation'),
    path('reservations/delete/<int:reservationId>', views.deleteReservation, name='deleteReservation'),

]
