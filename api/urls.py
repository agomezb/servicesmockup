from django.urls import path, include
from rest_framework import routers

from api.views import VentaViewSet, ProductoViewSet

router = routers.DefaultRouter()
router.register(r'venta', VentaViewSet)
router.register(r'producto', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]