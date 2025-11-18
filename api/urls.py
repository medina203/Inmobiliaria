from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'propiedades', views.PropiedadViewSet, basename='propiedades')
router.register(r'tipos-propiedad', views.TipoPropiedadViewSet, basename='tipos-propiedad')
router.register(r'caracteristicas', views.CaracteristicaViewSet, basename='caracteristicas')
router.register(r'agentes', views.AgenteViewSet, basename='agentes')
router.register(r'clientes', views.ClienteViewSet, basename='clientes')
router.register(r'intereses', views.InteresPropiedadViewSet, basename='intereses')

urlpatterns = [
    path('', include(router.urls)),
]
