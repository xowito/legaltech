from django.urls import path
from .views import home,demandas,nueva_demanda, detalle_demanda, editar_demanda, eliminar_demanda, ultima_demanda,welcome, registro, profile,crear_informe



urlpatterns = [
    path('welcome',welcome,name='welcome'),
    path('', home, name='home'),
    path('nueva_demanda', nueva_demanda, name='nueva_demanda'),
    path('demandas',demandas,name='demandas'),
    path('detalle_demanda/<id>/',detalle_demanda,name='detalle_demanda'),
    path('editar_demanda/<id>/',editar_demanda,name='editar_demanda'),
    path('eliminar_demanda/<id>/',eliminar_demanda,name='eliminar_demanda'),
    path('registro',registro, name='registro'),
    path('profile',profile,name='profile'),
    path('ultima_demanda',ultima_demanda,name='ultima_demanda'),
    path('crear_informe',crear_informe, name='crear_informe')
]
