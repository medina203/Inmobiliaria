from django.contrib import admin

# Register your models here.
from .models import Propiedad, Agente

@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'precio', 'habitaciones', 'fecha_publicacion']
    list_filter = ['tipo', 'habitaciones']
    search_fields = ['titulo', 'direccion']

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'email']