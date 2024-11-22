from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
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

class TipoUsuario(models.TextChoices):
   PROPIETARIO = 'P','Propietario'
   ARRENDATARIO = 'A','Arrendatario'

class TipoInmueble(models.TextChoices):
   CASA = 'C','Casa'
   DEPARTAMENTO = 'D','Departamento'
   PARCELA = 'P','Parcela'

class Usuario(models.Model):
   user = models.OneToOneField(User, on_delete= models.CASCADE)
   rut = models.CharField(max_length=10, null=False, blank=False)
   second_name = models.CharField(max_length=50, null=False, default='')
   telefono = models.CharField(max_length=50, null=False, default='')
   direccion = models.CharField(max_length=255, null=True, blank=True)
   tipo_usuario = models.CharField(max_length=1, choices=TipoUsuario.choices,null=False, blank=False,default='A')
   def __str__(self):
      return self.user.first_name
   

def create_user_profile(sender, instance, created, **kwargs):
   if created:
      Usuario.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
   instance.usuario.save()

post_save.connect(create_user_profile, sender=Usuario)
post_save.connect(save_user_profile, sender=Usuario)


class Inmueble(models.Model):
    nombre = models.ForeignKey(Usuario.__name__,on_delete=models.CASCADE)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    comuna = models.OneToOneField(Comuna, on_delete=models.CASCADE)
    tipo_inmueble = models.CharField(max_length=1, choices=TipoInmueble.choices, null=False, blank=False, default='C')
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
     return self.nombre
    