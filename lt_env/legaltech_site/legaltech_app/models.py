from django.db import models

# Create your models here.
tipos_de_demanda = [
    ('1','Demanda de marca'),
	('2','Demanda de linea'),
	('3','Demanda de empresa'),
	('4','Demanda global'),
	('5','Demanda individual'),
	('6','Demanda de segmento'),
	('7','Demanda de mercado'),
	('8','Demanda total'),
	]
comunas = [
    ('1','Talcahuano'),
	('2','Concepcion'),
	('3','Chiguayante'),
    ('4','Hualpen'),]
class Demanda(models.Model):
    Id = models.IntegerField(primary_key = True)#edit to charfield
    Hora = models.CharField (max_length=6)
    Fecha = models.DateField(auto_now_add=True)
    Tipo_de_demanda = models.CharField(default=1,max_length=1, choices = tipos_de_demanda)
    Rut_demandado = models.CharField(max_length=10)
    Nombre_demandado = models.CharField(max_length=50)
    Apellido_demandado = models.CharField(max_length=50)
    Telefono_demandado = models.IntegerField()
    Comuna_demandado = models.CharField(default=1,max_length=1, choices = comunas)
    Rut_demandante = models.CharField(max_length=10)
    Nombre_demandante = models.CharField(max_length=50)
    Apellido_demandante = models.CharField(max_length=50)
    Telefono_demandante = models.IntegerField()
    Comuna_demandante = models.CharField(default=1,max_length=1, choices = comunas)
    Detalle_demanda = models.CharField(max_length= 500)

def __str__(self):
	return self.Nombre_demandante