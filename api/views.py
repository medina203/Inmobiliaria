from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from propiedades.models import Propiedad, TipoPropiedad, Caracteristica
from agentes.models import Agente
from clientes.models import Cliente, InteresPropiedad
from propiedades.serializers import (
    PropiedadSerializer, PropiedadListSerializer, TipoPropiedadSerializer, CaracteristicaSerializer
)
from agentes.serializers import AgenteSerializer
from clientes.serializers import ClienteSerializer, InteresPropiedadSerializer

class PropiedadViewSet(viewsets.ModelViewSet):
    """
    API endpoint para gestionar propiedades
    """
    queryset = Propiedad.objects.all().select_related('tipo_propiedad', 'agente').prefetch_related('caracteristicas', 'imagenes')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tipo_propiedad', 'tipo_operacion', 'estado', 'comuna', 'ciudad', 'destacado']
    search_fields = ['titulo', 'descripcion', 'direccion', 'comuna', 'ciudad']
    ordering_fields = ['precio_venta', 'precio_arriendo', 'fecha_publicacion', 'visitas']
    ordering = ['-fecha_publicacion']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return PropiedadListSerializer
        return PropiedadSerializer

class TipoPropiedadViewSet(viewsets.ModelViewSet):
    queryset = TipoPropiedad.objects.all()
    serializer_class = TipoPropiedadSerializer

class CaracteristicaViewSet(viewsets.ModelViewSet):
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializer

class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.filter(activo=True)
    serializer_class = AgenteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'apellido', 'email', 'especialidades']
    ordering_fields = ['fecha_contratacion', 'total_transacciones']
    ordering = ['apellido', 'nombre']

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.filter(activo=True)
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['tipo_cliente']
    search_fields = ['nombre', 'apellido', 'email', 'telefono']

class InteresPropiedadViewSet(viewsets.ModelViewSet):
    queryset = InteresPropiedad.objects.all().select_related('cliente', 'propiedad')
    serializer_class = InteresPropiedadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cliente', 'propiedad', 'contactado']
