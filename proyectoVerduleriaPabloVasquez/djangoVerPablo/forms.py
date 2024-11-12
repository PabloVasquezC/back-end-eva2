from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.CharField()
    stock = forms.IntegerField()
    categoria = forms.CharField()
    estado= forms.CharField()
    observaciones= forms.CharField()
    proveedores= forms.CharField()


    nombre.widget.attrs['class']='form-control'
    descripcion.widget.attrs['class']='form-control'
    precio.widget.attrs['class']='form-control'
    stock.widget.attrs['class']='form-control'
    categoria.widget.attrs['class']='form-control'
    estado.widget.attrs['class']='form-control'
    observaciones.widget.attrs['class']='form-control'
    proveedores.widget.attrs['class']='form-control'

class ClienteForm(forms.Form):
    nombre_cliente = forms.CharField()
    correo = forms.EmailField()
    telefono = forms.CharField()
    direccion = forms.CharField()
    ciudad = forms.CharField()
    pais= forms.CharField()
    fecha_registro= forms.DateField()
    tipo_cliente= forms.CharField()
    preferencias= forms.CharField()
    fecha_nacimiento= forms.DateField()
    genero= forms.CharField()


    nombre_cliente.widget.attrs['class']='form-control'
    correo.widget.attrs['class']='form-control'
    telefono.widget.attrs['class']='form-control'
    direccion.widget.attrs['class']='form-control'
    ciudad.widget.attrs['class']='form-control'
    pais.widget.attrs['class']='form-control'
    fecha_registro.widget.attrs['class']='form-control'
    tipo_cliente.widget.attrs['class']='form-control'
    preferencias.widget.attrs['class']='form-control'
    fecha_nacimiento.widget.attrs['class']='form-control'
    genero.widget.attrs['class']='form-control'
