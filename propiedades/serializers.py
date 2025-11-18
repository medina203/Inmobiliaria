from rest_framework import serializers
from .models import Propiedad, TipoPropiedad, Caracteristica, ImagenPropiedad

class CaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica
        fields = '__all__'

class TipoPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPropiedad
        fields = '__all__'

class ImagenPropiedadSerializer(serializers.ModelSerializer):
    imagen_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ImagenPropiedad
        fields = ['id', 'imagen', 'imagen_url', 'orden', 'es_principal']
    
    def get_imagen_url(self, obj):
        request = self.context.get('request')
        if obj.imagen:
            return request.build_absolute_uri(obj.imagen.url)
        return None

class PropiedadSerializer(serializers.ModelSerializer):
    tipo_propiedad_nombre = serializers.CharField(source='tipo_propiedad.nombre', read_only=True)
    agente_nombre = serializers.CharField(source='agente.nombre_completo', read_only=True)
    caracteristicas = CaracteristicaSerializer(many=True, read_only=True)
    imagenes = ImagenPropiedadSerializer(many=True, read_only=True)
    precio = serializers.SerializerMethodField()
    
    class Meta:
        model = Propiedad
        fields = [
            'id', 'titulo', 'descripcion', 'tipo_propiedad', 'tipo_propiedad_nombre',
            'tipo_operacion', 'precio_venta', 'precio_arriendo', 'precio',
            'direccion', 'comuna', 'ciudad', 'region', 'latitud', 'longitud',
            'habitaciones', 'banos', 'estacionamientos', 'superficie_total',
            'superficie_construida', 'estado', 'agente', 'agente_nombre',
            'fecha_publicacion', 'caracteristicas', 'imagenes', 'visitas', 'destacado'
        ]
    
    def get_precio(self, obj):
        return obj.obtener_precio()

class PropiedadListSerializer(serializers.ModelSerializer):
    tipo_propiedad_nombre = serializers.CharField(source='tipo_propiedad.nombre', read_only=True)
    precio = serializers.SerializerMethodField()
    imagen_principal = serializers.SerializerMethodField()
    
    class Meta:
        model = Propiedad
        fields = [
            'id', 'titulo', 'tipo_propiedad_nombre', 'tipo_operacion',
            'precio', 'direccion', 'comuna', 'ciudad', 'habitaciones',
            'banos', 'estacionamientos', 'superficie_total', 'estado',
            'imagen_principal', 'destacado', 'fecha_publicacion'
        ]
    
    def get_precio(self, obj):
        return obj.obtener_precio()
    
    def get_imagen_principal(self, obj):
        request = self.context.get('request')
        imagen_principal = obj.imagenes.filter(es_principal=True).first()
        if imagen_principal and imagen_principal.imagen:
            return request.build_absolute_uri(imagen_principal.imagen.url)
        return None
