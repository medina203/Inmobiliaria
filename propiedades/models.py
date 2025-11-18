from django.db import models
from agentes.models import Agente

class TipoPropiedad(models.Model):
    """Tipos de propiedades: Casa, Departamento, Terreno, etc."""
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Tipo de Propiedad"
        verbose_name_plural = "Tipos de Propiedades"
    
    def __str__(self):
        return self.nombre

class Caracteristica(models.Model):
    """Características adicionales: Piscina, Garaje, etc."""
    nombre = models.CharField(max_length=50, unique=True)
    icono = models.CharField(max_length=30, blank=True, help_text="Nombre del icono")
    
    class Meta:
        verbose_name = "Característica"
        verbose_name_plural = "Características"
    
    def __str__(self):
        return self.nombre

class Propiedad(models.Model):
    """Modelo principal de propiedades inmobiliarias"""
    
    TIPO_OPERACION = [
        ('venta', 'Venta'),
        ('arriendo', 'Arriendo'),
        ('venta_arriendo', 'Venta o Arriendo'),
    ]
    
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('vendida', 'Vendida'),
        ('arrendada', 'Arrendada'),
        ('reservada', 'Reservada'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo_propiedad = models.ForeignKey(TipoPropiedad, on_delete=models.PROTECT)
    tipo_operacion = models.CharField(max_length=20, choices=TIPO_OPERACION)
    
    # Precios
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    precio_arriendo = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    # Ubicación
    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    latitud = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitud = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    
    # Características principales
    habitaciones = models.IntegerField(default=0)
    banos = models.IntegerField(default=0, verbose_name="Baños")
    estacionamientos = models.IntegerField(default=0)
    superficie_total = models.IntegerField(help_text="Superficie en metros cuadrados")
    superficie_construida = models.IntegerField(help_text="Superficie construida en metros cuadrados", null=True, blank=True)
    
    # Estado y agente
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    agente = models.ForeignKey(Agente, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Fechas
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    # Características adicionales
    caracteristicas = models.ManyToManyField(Caracteristica, blank=True)
    
    # Visitas y destacado
    visitas = models.IntegerField(default=0)
    destacado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"
        ordering = ['-destacado', '-fecha_publicacion']
    
    def __str__(self):
        return f"{self.titulo} - {self.comuna}"
    
    def obtener_precio(self):
        """Retorna el precio según tipo de operación"""
        if self.tipo_operacion == 'venta':
            return self.precio_venta
        elif self.tipo_operacion == 'arriendo':
            return self.precio_arriendo
        return self.precio_venta or self.precio_arriendo

class ImagenPropiedad(models.Model):
    """Imágenes de las propiedades"""
    propiedad = models.ForeignKey(Propiedad, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='propiedades/%Y/%m/')
    orden = models.IntegerField(default=0)
    es_principal = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Imagen de Propiedad"
        verbose_name_plural = "Imágenes de Propiedades"
        ordering = ['orden']
    
    def __str__(self):
        return f"Imagen {self.id} - {self.propiedad.titulo}"
