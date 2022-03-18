from django.urls import path
from .views import home,demandas 



urlpatterns = [
    path('', home, name='home'),
    path('demandas',demandas,name='demandas')
]