from django.shortcuts import render,redirect, get_object_or_404
from .models import Demanda
from .forms import demanda_form, registro_form
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    return render(request,'legaltech_app/home.html')
def welcome(request):
    return render(request,'legaltech_app/welcome.html')

def nueva_demanda(request):
    formulario = demanda_form()
    data={"form":formulario}
    
    if request.method == 'POST':
        formulario = demanda_form(data=request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="home")
    return render (request, 'legaltech_app/nueva_demanda.html',data)

def demandas(request):
    demanda = Demanda.objects.all()
    data = {"obj":demanda}
    return render(request,'legaltech_app/demandas.html',data)

def detalle_demanda(request,id):
    detalle = Demanda.objects.get(Id=id)
    data = {"obj":detalle}
    return render(request,'legaltech_app/detalle_demanda.html',data)
    
def editar_demanda(request,id):
    demanda = get_object_or_404(Demanda,Id=id)
    data = {
        "form":demanda_form(instance=demanda)
    }
    if request.method == 'POST':
        formulario = demanda_form(data=request.POST, instance=demanda)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="demandas")
        data["form"]=formulario
    return render(request,'legaltech_app/editar_demanda.html',data)

def eliminar_demanda(request,id):
    demanda = get_object_or_404(Demanda,Id=id)
    demanda.delete()
    return redirect(to="demandas")

def registro(request):
    data={"form": registro_form()}
    
    if request.method =='POST':
        formulario = registro_form(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="login")
        data['form'] = formulario
    return render(request,'registration/registro.html',data)