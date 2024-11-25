from django.contrib import admin
from .models import  Inmueble, Region, Comuna
# Register your models here.

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre_inmueble', 'direccion', 'precio')
    search_fields = ('nombre_inmueble', 'direccion')
    # list_filter = ('precio', 'region')

admin.site.register(Region)
admin.site.register(Comuna)
