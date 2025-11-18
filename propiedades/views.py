from django.shortcuts import render
from .models import Propiedad

def lista_propiedades(request):
    propiedades = Propiedad.objects.all().order_by('-fecha_publicacion')
    return render(request, 'propiedades/lista_propiedades.html', {'propiedades': propiedades})