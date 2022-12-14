from django.urls import path
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('rooms/', views.rooms_index, name='rooms'),
    path('rooms/<int:roomId>', views.roomDetails_index, name='roomDetails'),
    path('rooms/<int:roomId>/checkOut', views.checkOut, name='checkOut'),
]