from django import forms
from .models import Room, Client, Reservation

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['price', 'occupied', 'number']
        
        widgets = {
            'price': forms.TextInput(attrs={'class': 'form__input'}),
            'occupied': forms.HiddenInput(attrs={'value':False}),
            'number': forms.TextInput(attrs={'class': 'form__input'}),
        }
        labels = {
            'price': 'Cena za dobę',
            'occupied': '',
            'number': 'Numer pokoju',
        }
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['dateFrom', 'dataTo', 'client']
        widgets = {
            'dateFrom': forms.TextInput(attrs={'class': 'form__input'}),
            'dataTo': forms.TextInput(attrs={'class': 'form__input'}),

        }
        labels = {
            'dateFrom': 'Date zameldowania',
            'dataTo': 'Date wymeldowania'
            
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form__input'}),
            'last_name': forms.TextInput(attrs={'class': 'form__input'}),
            'birth_date': forms.DateInput(attrs={'class': 'form__input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form__input'}),
        }
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'birth_date': 'Data urodzenia (DD/MM/RRRR)',
            'phone_number': 'Numer telefonu',
        }