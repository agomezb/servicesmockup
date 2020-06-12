from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers
from servicemockup.models import Venta, Producto


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = serializers.VentaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        referencia = self.request.query_params.get("referencia", None)
        if referencia:
            queryset = queryset.filter(referencia__icontains=referencia)
        return queryset


class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = serializers.ProductoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro = self.request.query_params.get("search", None)
        if filtro:
            queryset = queryset.filter(nombre__icontains=filtro)
        return queryset.order_by('-nombre')


class VerificarVentaView(APIView):

    def get(self, request):
        referencia = self.request.query_params.get('referencia', None)
        ventaquery = Venta.objects.filter(referencia=referencia)
        if ventaquery:
            venta = ventaquery[0]
            return Response({'id': venta.id})
        return Response({'detail':'No existe venta'}, status=status.HTTP_404_NOT_FOUND)