
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Persona(BaseModel):
    CLIENTE_NATURAL = 'N'
    CLIENTE_JURIDICO = 'J'
    CLIENTE_PLACA = 'P'
    COD_CONSUMIDOR_FINAL = '07'

    TIPO_CLIENTE = (
        (CLIENTE_NATURAL, 'Natural'),
        (CLIENTE_JURIDICO, 'Juridico')
    )

    ID_CEDULA = 'CED'
    ID_PASAPORTE = 'PAS'
    ID_RUC = 'RUC'

    tipo_cliente = models.CharField(max_length=1,
                                    choices=TIPO_CLIENTE,
                                    default=CLIENTE_NATURAL)

    identificacion = models.CharField(max_length=50, unique=True)

    nombre = models.CharField(max_length=200)

    correo = models.CharField(max_length=50,
                              null=True,
                              blank=True)

    telefono = models.CharField(max_length=22,
                                null=True,
                                blank=True)

    direccion = models.CharField(max_length=150,
                                 null=True,
                                 blank=True)

    extranjero = models.BooleanField(default=False)


class Producto(BaseModel):
    ACTIVO = 'A'
    INACTIVO = 'I'

    ESTADOS = (
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inactivo')
    )

    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    stock = models.PositiveSmallIntegerField(default=0)
    precio = models.PositiveSmallIntegerField(default=0)
    iva = models.PositiveSmallIntegerField(default=0)
    categoria = models.CharField(max_length=50)
    estado = models.CharField(max_length=1, choices=ESTADOS, default=ACTIVO)


class Venta(BaseModel):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='+')
    fecha_hora_venta = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, related_name='+')


class DetalleVenta(BaseModel):

    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveSmallIntegerField(default=0)
    descripcion = models.CharField(max_length=200)