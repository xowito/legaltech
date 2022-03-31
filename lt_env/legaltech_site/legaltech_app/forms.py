from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User
class demanda_form(forms.ModelForm):
    Detalle_demanda = forms.CharField(max_length= 500,widget=forms.Textarea)

    class Meta:
        model=Demanda
        fields= '__all__'
    
class registro_form(UserCreationForm):
    username = forms.CharField(max_length=10,label="Rut",
                               widget=forms.TextInput(attrs={'placeholder': 'Rut sin puntos y con guion, ejemplo:12345678-9'}))
    class Meta:
        model = User
        fields=['username','first_name', 'last_name','email','password1','password2' ]