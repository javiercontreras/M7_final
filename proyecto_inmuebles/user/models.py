from django.db import models
from django.contrib.auth.admin import User
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

class TipoUsuario(models.TextChoices):
   PROPIETARIO = 'P','Propietario'
   ARRENDATARIO = 'A','Arrendatario'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    rut = models.CharField(max_length=10, null=False, blank=False)
    second_name = models.CharField(max_length=50, null=False, default='')
    telefono = models.CharField(max_length=50, null=False, default='')
    direccion = models.CharField(max_length=255, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=1, choices=TipoUsuario.choices, null=False, blank=False,default='A')

    def __str__(self):
        return self.user.username

#  When a user instance is created django will send a signal
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=UserProfile)
def add_user_group(sender, instance, created, **kwargs):
        try:
            arrendatario_group = Group.objects.get(name='Arrendatario')
            
        except Group.DoesNotExist:
            arrendatario_group = Group.objects.create(name='Arrendatario')
            propietario_group = Group.objects.create(name='Propietario')
        instance.user.groups.add(arrendatario_group)