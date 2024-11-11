from django.db import models
from django import forms

# Create your models here.
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha = models.DateField()
    fecha_registro = models.DateField()
    tipo_cliente = models.CharField(max_length=100)
    preferencias = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    proveedores = models.CharField(max_length=100)







