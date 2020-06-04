from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'venta', VentaViewSet)
router.register(r'producto', ViajesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]