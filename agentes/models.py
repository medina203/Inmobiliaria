from django.db import models
from django.contrib.auth.models import User

class Agente(models.Model):
    """Agentes inmobiliarios"""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    telefono_secundario = models.CharField(max_length=20, blank=True)
    
    # Información profesional
    foto = models.ImageField(upload_to='agentes/', null=True, blank=True)
    licencia = models.CharField(max_length=50, unique=True)
    fecha_contratacion = models.DateField()
    activo = models.BooleanField(default=True)
    
    # Redes sociales
    whatsapp = models.CharField(max_length=20, blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    
    # Descripción y especialidades
    descripcion = models.TextField(blank=True)
    especialidades = models.CharField(max_length=255, help_text="Ej: Casas, Departamentos, Terrenos")
    
    # Estadísticas
    propiedades_vendidas = models.IntegerField(default=0)
    propiedades_arrendadas = models.IntegerField(default=0)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Agente"
        verbose_name_plural = "Agentes"
        ordering = ['apellido', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def total_transacciones(self):
        return self.propiedades_vendidas + self.propiedades_arrendadas
