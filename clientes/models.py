from django.db import models
from propiedades.models import Propiedad

class Cliente(models.Model):
    """Clientes potenciales o registrados"""
    
    TIPO_CLIENTE = [
        ('comprador', 'Comprador'),
        ('arrendatario', 'Arrendatario'),
        ('vendedor', 'Vendedor'),
        ('propietario', 'Propietario'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    telefono_secundario = models.CharField(max_length=20, blank=True)
    
    tipo_cliente = models.CharField(max_length=20, choices=TIPO_CLIENTE)
    
    # Preferencias
    tipo_propiedad_interes = models.ManyToManyField('propiedades.TipoPropiedad', blank=True)
    rango_precio_min = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    rango_precio_max = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    # Ubicación de interés
    comunas_interes = models.TextField(blank=True, help_text="Comunas de interés separadas por comas")
    
    # Estado
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    # Notas
    notas = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-fecha_registro']
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.email}"

    def nombre_completo(self):          # <-- añadir
        return f"{self.nombre} {self.apellido}"
    nombre_completo.short_description = "Nombre completo"


class InteresPropiedad(models.Model):
    """Registra el interés de un cliente en una propiedad"""
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE)
    fecha_interes = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(blank=True)
    contactado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Interés en Propiedad"
        verbose_name_plural = "Intereses en Propiedades"
        unique_together = ['cliente', 'propiedad']
    
    def __str__(self):
        return f"{self.cliente} interesado en {self.propiedad}"
