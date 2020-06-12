from django.urls import path, include
from rest_framework import routers

from api.views import VentaViewSet, ProductoViewSet, VerificarVentaView

router = routers.DefaultRouter()
router.register(r'venta', VentaViewSet)
router.register(r'producto', ProductoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("verificar-venta/", VerificarVentaView.as_view(), name="verificar_venta"),
]