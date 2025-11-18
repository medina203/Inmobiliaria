from django.contrib import admin
from .models import Cliente, InteresPropiedad

class InteresPropiedadInline(admin.TabularInline):
    model = InteresPropiedad
    extra = 0
    readonly_fields = ['fecha_interes']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_completo', 'email', 'telefono', 'tipo_cliente', 'activo', 'fecha_registro'
    ]
    list_filter = ['tipo_cliente', 'activo', 'fecha_registro', 'tipo_propiedad_interes']
    search_fields = ['nombre', 'apellido', 'email', 'telefono']
    readonly_fields = ['fecha_registro']
    inlines = [InteresPropiedadInline]

@admin.register(InteresPropiedad)
class InteresPropiedadAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'propiedad', 'fecha_interes', 'contactado']
    list_filter = ['contactado', 'fecha_interes']
    search_fields = ['cliente__nombre', 'cliente__apellido', 'propiedad__titulo']
