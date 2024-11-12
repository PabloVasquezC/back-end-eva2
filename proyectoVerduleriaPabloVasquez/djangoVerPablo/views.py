from djangoVerPablo.forms import ProductoForm
from djangoVerPablo.forms import ClienteForm
from django.shortcuts import render
from djangoVerPablo.models import Producto
from djangoVerPablo.models import Cliente
from django.urls import reverse
from django.http import HttpResponseRedirect







def index(request):
    return render(request, 'djangoVerPablo/index.html')

def form(request):
    return render(request, 'djangoVerPablo/form.html')

# def clienteData(request):
#     clientes = Cliente.objects.all()
#     data = {'clientes': clientes}
#     return render(request, 'djangoVerPablo/clientes.html', data)

# def agregar_cliente(request):
#     form=ClienteForm()

#     if request.method=='POST':
#         form=ClienteForm(request.POST)
#         if form.is_valid():
#             Cliente.objects.create(
#                 nombre_cliente=form.cleaned_data['nombre_cliente'],
#                 correo=form.cleaned_data['correo'],
#                 telefono=form.cleaned_data['telefono'],
#                 direccion=form.cleaned_data['direccion'],
#                 ciudad=form.cleaned_data['ciudad'],
#                 pais=form.cleaned_data['pais'],
#                 fecha_registro=form.cleaned_data['fecha_registro'],
#                 tipo_cliente=form.cleaned_data['tipo_cliente'],
#                 preferencias=form.cleaned_data['preferencias'],
#                 fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
#                 genero=form.cleaned_data['genero'],
#             )
#             return HttpResponseRedirect(reverse('clienteData'))


#     data={'form':form}
#     return render(request, 'djangoVerPablo/registroClientes.html',data)



def productos(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'djangoVerPablo/productos.html', data)

def agregarProducto(request):
    form=ProductoForm()

    if request.method=='POST':
        form=ProductoForm(request.POST)
        if form.is_valid():
            Producto.objects.create(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],
                stock=form.cleaned_data['stock'],
                categoria=form.cleaned_data['categoria'],
                estado=form.cleaned_data['estado'],
                observaciones=form.cleaned_data['observaciones'],
                proveedores=form.cleaned_data['proveedores'],
            )
            return HttpResponseRedirect(reverse('productos'))
    data={'form':form}
    return render(request, 'djangoVerPablo/agregarProducto.html',data)
