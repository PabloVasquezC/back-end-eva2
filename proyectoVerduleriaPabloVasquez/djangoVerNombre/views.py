from django.shortcuts import render, redirect
from django import forms
from .forms import ProductoForm

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista_productos')  
    else:
        form = ProductoForm()
    
    return render(request, 'agregar_producto.html', {'form': form})




def index(request):
    return render(request, 'djangoVerNombre/index.html')

def form(request):
    return render(request, 'djangoVerNombre/form.html')

