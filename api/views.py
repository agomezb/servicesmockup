from django.shortcuts import render
from rest_framework import viewsets

from servicemockup.models import Venta


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = serializers.VentaSerializer
