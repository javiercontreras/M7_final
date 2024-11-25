from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from user.models import UserProfile

# Create your models here.
class Region(models.Model):
   nombre = models.TextField(null=False, blank=False)

   def __str__(self):
      return self.nombre

class Comuna(models.Model):
   nombre = models.TextField(null=False, blank=False)
   region = models.ForeignKey(Region, on_delete=models.CASCADE)
   
   def __str__(self):
      return self.nombre


class TipoInmueble(models.TextChoices):
   CASA = 'C','Casa'
   DEPARTAMENTO = 'D','Departamento'
   PARCELA = 'P','Parcela'


class Inmueble(models.Model):
    nombre = models.ForeignKey(User,on_delete=models.CASCADE)
    nombre_inmueble = models.CharField(max_length=100, null=False, blank=False, default='')
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    tipo_inmueble = models.CharField(max_length=1, choices=TipoInmueble.choices, null=False, blank=False, default='C')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
     return self.nombre_inmueble
    