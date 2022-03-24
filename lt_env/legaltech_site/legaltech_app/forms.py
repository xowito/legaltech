from django import forms
from .models import *

class demanda_form(forms.ModelForm):
    Detalle_demanda = forms.CharField(max_length= 500,widget=forms.Textarea)

    class Meta:
        model=Demanda
        fields= '__all__'
    