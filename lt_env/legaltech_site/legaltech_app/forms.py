from django import forms
from django.contrib.auth.forms import UserCreationForm

from legaltech_app.MinimalSplitDateTimeMultiWidget import MinimalSplitDateTimeMultiWidget
from .models import *
from django.contrib.auth.models import User
from django.contrib.admin import widgets
class demanda_form(forms.ModelForm):
    Detalle_demanda = forms.CharField(max_length= 500,widget=forms.Textarea)
    Fecha = forms.DateTimeField(widget=MinimalSplitDateTimeMultiWidget(attrs={"class":"form-control"}))
    Telefono_demandado = forms.IntegerField(widget=forms.TextInput(attrs={'type':'tel','pattern':'+[0-9]{3}[0-9]{8}','title':'Debe ser un numero valido'}))
    Telefono_demandante = forms.IntegerField(widget=forms.TextInput(attrs={'type':'tel','pattern':'+[0-9]{3}[0-9]{8}','title':'Debe ser un numero valido'}))
    class Meta:
        model=Demanda
        fields= '__all__'
           
class registro_form(UserCreationForm):
    username = forms.CharField(max_length=10,label="Rut",
                               widget=forms.TextInput(attrs={'placeholder': 'Rut sin puntos y con guion, ejemplo:12345678-9'}))
    class Meta:
        model = User
        fields=['username','first_name', 'last_name','email','password1','password2' ]