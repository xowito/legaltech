from django.shortcuts import render,redirect, get_object_or_404
from .models import Demanda
from .forms import demanda_form, registro_form
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
            messages.success(request, "Demanda ingresada correctamente!")
            return redirect(to="demandas")
    return render (request, 'legaltech_app/nueva_demanda.html',data)

def demandas(request):
    qs = Demanda.objects.all()
    Id_contains_query = request.GET.get('Id_contiene')
    Fecha_contiene_query = request.GET.get('Fecha_contiene')
    
    
    if Id_contains_query != '' and Id_contains_query is not None:
        qs = qs.filter(Id__icontains=Id_contains_query)
    elif Fecha_contiene_query != '' and Fecha_contiene_query is not None:
        qs = qs.filter(Fecha__icontains=Fecha_contiene_query)
    contexto = {
        'queryset': qs
    }
    
    return render(request,'legaltech_app/demandas.html',contexto)

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
            messages.success(request, "Demanda modificada correctamente!")
            return redirect(to="demandas")
        data["form"]=formulario
    return render(request,'legaltech_app/editar_demanda.html',data)

def eliminar_demanda(request,id):
    demanda = get_object_or_404(Demanda,Id=id)
    demanda.delete()
    messages.success(request,"Demanda eliminada correctamente!")
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

def profile(request):
    return render(request,'legaltech_app/profile.html')
