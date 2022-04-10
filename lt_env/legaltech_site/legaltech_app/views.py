from django.shortcuts import render,redirect, get_object_or_404
from .models import Demanda
from .forms import demanda_form, registro_form
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4

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
        else:
            messages.error(request, "Hubo un error, vuelve a intentarlo")
    return render (request, 'legaltech_app/nueva_demanda.html',data)

def is_valid_queryparam(param):
    return param != '' and param is not None
def demandas(request):
    qs = Demanda.objects.all()
    Id_contiene_query = request.GET.get('Id_contiene')
    Fecha_contiene_query = request.GET.get('Fecha_contiene')
    
    if is_valid_queryparam(Id_contiene_query):
        qs = qs.filter(Id__icontains=Id_contiene_query)
    elif is_valid_queryparam(Fecha_contiene_query):
        qs = qs.filter(Fecha__icontains=Fecha_contiene_query)

    contexto = {
        'queryset': qs
    }
    
    return render(request,'legaltech_app/demandas.html',contexto)
def ultima_demanda(request):
    contexto ={
        'demandas':Demanda.objects.last()
    }
    return render(request,'legaltech_app/ultima_demanda.html',contexto)
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
    messages.success(request,"Demanda eliminada exitosamente!")
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

def crear_informe(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter,bottomup=0)
    textob = c.beginText(inch, inch)
    textob.setTextOrigin(inch, inch)

    textob.setFont("Helvetica", 14)
    
    demandas = Demanda.objects.all()
    
    lines = []
    
    for demanda in demandas:
        lines.append("Info Demanda")
        lines.append("Id: " + demanda.Id)
        lines.append("Hora: " + demanda.Hora)
        lines.append(f"Fecha: {demanda.Fecha}" )
        lines.append("Tipo de demanda: " + f"{demanda.get_Tipo_de_demanda_display()}")
        lines.append("-------------------------------------------------------------------")
        lines.append("Info Demandandado")
        lines.append("Rut: "+demanda.Rut_demandado)
        lines.append("Nombre demandado: " + demanda.Nombre_demandado + " " + demanda.Apellido_demandado)
        lines.append(f"Telefono: {demanda.Telefono_demandado}" )
        lines.append("Comuna: " + f"{demanda.get_Comuna_demandado_display()}" )
        lines.append("-------------------------------------------------------------------")
        lines.append("Info Demandante")
        lines.append("Rut: "+demanda.Rut_demandante)
        lines.append("Nombre demandante: " + demanda.Nombre_demandante + " " + demanda.Apellido_demandante)
        lines.append(f"Telefono: {demanda.Telefono_demandante}" )
        lines.append("Comuna: " + f"{demanda.get_Comuna_demandante_display()}" )
        lines.append("-------------------------------------------------------------------")
        lines.append("Detalle demanda: " + demanda.Detalle_demanda)
        lines.append(" ")
        lines.append(" ")
        lines.append(" ")
        lines.append("--------------------------------------------------------------------------------------")
        
    for line in lines:
        textob.textLine(line) 
    c.drawText(textob)
    c.save()
    c.showPage()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='Demandas.pdf')