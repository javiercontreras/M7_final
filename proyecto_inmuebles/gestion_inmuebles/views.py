from django.shortcuts import render
from .models import Inmueble, Region, Comuna
# Create your views here.
def indice(request):      
    inmuebles = Inmueble.objects.all()      
    region = request.GET.get('region','')
    if region:
        inmuebles = inmuebles.filter(region__nombre__icontains = region)

    
    regiones = Region.objects.all()
    return render(request,'index.html',{'inmuebles':inmuebles, 'regiones':regiones})