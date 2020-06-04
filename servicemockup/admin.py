from django.contrib import admin

from servicemockup.models import Producto, Persona, Venta, DetalleVenta


class DeatlleVentaInline(admin.TabularInline):
    model = DetalleVenta


class VentaAdmin(admin.ModelAdmin):
    inlines = (
        DeatlleVentaInline,
    )


admin.site.register(Persona)
admin.site.register(Producto)
admin.site.register(Venta, VentaAdmin)
