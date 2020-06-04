from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.transaction import atomic
from rest_framework import serializers

from servicemockup.models import Persona, DetalleVenta, Venta


class SincronizacionException(Exception):
    pass


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id', 'identificacion', 'nombre', 'correo', 'direccion', 'telefono', 'extranjero')
        extra_kwargs = {
            'identificacion': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class DetalleVentaSerializer(serializers.ModelSerializer):

    @staticmethod
    def generate(venta, validated_data):
        boleto = DetalleVenta.objects.create(venta=venta, **validated_data)
        return boleto

    class Meta:
        model = DetalleVenta
        fields = (
            'id',
            'producto',
            'cantidad',
            'descripcion'
        )


class VentaSerializer(serializers.ModelSerializer):
    detalles = DetalleVentaSerializer(many=True, required=True, allow_null=False)
    persona = PersonaSerializer(many=False, required=True, allow_null=False)

    @atomic
    def create(self, validated_data):
        request = self.context['request']
        try:
            personadata = validated_data.pop('persona')
            persona = PersonaSerializer.generate(personadata)
            detalles = validated_data.pop('detalles')
            venta = Venta.objects.create(persona=persona, **validated_data)
            for detalledata in detalles:
                DetalleVentaSerializer.generate(request, venta, detalledata)
        except SincronizacionException as e:
            raise serializers.ValidationError({'detail': str(e)})

        return venta

    class Meta:
        model = Venta
        fields = ('id', 'detalles', 'persona')
