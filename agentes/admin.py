from django.contrib import admin
from .models import Agente

@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_completo', 'email', 'telefono', 'activo',
        'total_transacciones', 'fecha_contratacion'
    ]
    list_filter = ['activo', 'fecha_contratacion', 'especialidades']
    search_fields = ['nombre', 'apellido', 'email', 'licencia']
    readonly_fields = ['total_transacciones', 'fecha_creacion']
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('user', 'nombre', 'apellido', 'email', 'telefono', 'telefono_secundario', 'foto')
        }),
        ('Información Profesional', {
            'fields': ('licencia', 'fecha_contratacion', 'activo', 'descripcion', 'especialidades')
        }),
        ('Redes Sociales', {
            'fields': ('whatsapp', 'facebook', 'instagram', 'linkedin')
        }),
        ('Estadísticas', {
            'fields': ('propiedades_vendidas', 'propiedades_arrendadas', 'total_transacciones', 'fecha_creacion')
        }),
    )
