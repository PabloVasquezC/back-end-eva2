from django.contrib import admin
from .models import Producto, Cliente

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)

