from django.shortcuts import render
from .models import Demanda
from .forms import demanda_form
# Create your views here.
def home(request):
    formulario = demanda_form(request.POST)
    data={"form":formulario}
    return render (request, 'legaltech_app/nueva_demanda.html',data)

def demandas(request):
    demanda = Demanda.objects.all()
    data = {"obj":demanda}
    return render(request,'legaltech_app/demandas.html',data)