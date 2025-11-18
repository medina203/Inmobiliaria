from rest_framework import serializers
from .models import Cliente, InteresPropiedad

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class InteresPropiedadSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre_completo', read_only=True)
    propiedad_titulo = serializers.CharField(source='propiedad.titulo', read_only=True)
    
    class Meta:
        model = InteresPropiedad
        fields = ['id', 'cliente', 'cliente_nombre', 'propiedad', 'propiedad_titulo',
                  'fecha_interes', 'comentario', 'contactado']
