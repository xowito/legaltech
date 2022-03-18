from django import forms
from .models import *

class demanda_form(forms.ModelForm):
    class Meta:
        model=Demanda
        fields= '__all__'
    