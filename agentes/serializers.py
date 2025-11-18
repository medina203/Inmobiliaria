from rest_framework import serializers
from .models import Agente

class AgenteSerializer(serializers.ModelSerializer):
    nombre_completo = serializers.CharField(read_only=True)
    total_transacciones = serializers.IntegerField(read_only=True)
    foto_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Agente
        fields = [
            'id', 'nombre', 'apellido', 'nombre_completo', 'email', 'telefono',
            'telefono_secundario', 'foto', 'foto_url', 'licencia', 'fecha_contratacion',
            'activo', 'whatsapp', 'facebook', 'instagram', 'linkedin',
            'descripcion', 'especialidades', 'propiedades_vendidas',
            'propiedades_arrendadas', 'total_transacciones', 'fecha_creacion'
        ]
    
    def get_foto_url(self, obj):
        request = self.context.get('request')
        if obj.foto:
            return request.build_absolute_uri(obj.foto.url)
        return None
