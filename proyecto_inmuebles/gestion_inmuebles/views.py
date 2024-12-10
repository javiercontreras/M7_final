from django.shortcuts import render
from .models import Inmueble
# Create your views here.
def indice(request):
    inmuebles = Inmueble.objects.all()
    return render(request,'index.html',{'inmuebles':inmuebles})