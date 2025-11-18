from django.contrib import admin
from .models import Propiedad, TipoPropiedad, Caracteristica, ImagenPropiedad

class ImagenPropiedadInline(admin.TabularInline):
    model = ImagenPropiedad
    extra = 1
    fields = ['imagen', 'orden', 'es_principal']

@admin.register(TipoPropiedad)
class TipoPropiedadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'icono']
    search_fields = ['nombre']

@admin.register(Propiedad)
class PropiedadAdmin(admin.ModelAdmin):
    list_display = [
        'titulo', 'tipo_propiedad', 'tipo_operacion', 'comuna',
        'precio_venta', 'precio_arriendo', 'estado', 'destacado', 'visitas'
    ]
    list_filter = [
        'tipo_propiedad', 'tipo_operacion', 'estado', 'destacado',
        'comuna', 'ciudad', 'fecha_publicacion'
    ]
    search_fields = ['titulo', 'descripcion', 'direccion', 'comuna', 'ciudad']
    inlines = [ImagenPropiedadInline]
    filter_horizontal = ['caracteristicas']
    readonly_fields = ['fecha_publicacion', 'fecha_actualizacion', 'visitas']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'descripcion', 'tipo_propiedad', 'tipo_operacion', 'estado', 'destacado')
        }),
        ('Precios', {
            'fields': ('precio_venta', 'precio_arriendo')
        }),
        ('Ubicación', {
            'fields': ('direccion', 'comuna', 'ciudad', 'region', 'latitud', 'longitud')
        }),
        ('Características', {
            'fields': ('habitaciones', 'banos', 'estacionamientos', 'superficie_total', 'superficie_construida', 'caracteristicas')
        }),
        ('Agente y Fechas', {
            'fields': ('agente', 'visitas', 'fecha_publicacion', 'fecha_actualizacion')
        }),
    )
