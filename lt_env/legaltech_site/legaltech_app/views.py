from django.shortcuts import render
from.models import Demanda
# Create your views here.
def home(request):
    return render(request,'legaltech_app/home.html')


def demandas(request):
    demanda = Demanda.objects.all()
    data = {"obj":demanda}
    return render(request,'legaltech_app/demandas.html',data)