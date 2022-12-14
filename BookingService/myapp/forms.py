from django import forms
from .models import Room

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