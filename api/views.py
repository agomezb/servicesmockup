from rest_framework import viewsets
from api import serializers
from servicemockup.models import Venta, Producto


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = serializers.VentaSerializer


class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = serializers.ProductoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro = self.request.query_params.get("filtro", None)
        if filtro:
            queryset = queryset.filter(nombre__icontains=filtro)
        return queryset.order_by('-nombre')