from django.urls import path
from .views import home,demandas,nueva_demanda, detalle_demanda



urlpatterns = [
    path('', home, name='home'),
    path('nueva_demanda', nueva_demanda, name='nueva_demanda'),
    path('demandas',demandas,name='demandas'),
    path('detalle_demanda/<id>/',detalle_demanda,name='detalle_demanda')
]