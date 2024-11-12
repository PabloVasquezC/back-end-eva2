from django.contrib import admin
from .models import Producto, Cliente

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','precio','stock','categoria','estado','observaciones','proveedores')

admin.site.register(Producto, ProductoAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente','correo','telefono','direccion','ciudad','pais','fecha_registro','tipo_cliente','preferencias','fecha_nacimiento','genero')

admin.site.register(Cliente, ClienteAdmin)

