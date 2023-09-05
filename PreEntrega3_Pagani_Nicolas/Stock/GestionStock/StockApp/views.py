from django.shortcuts import render, redirect
from .forms import ProductoForm
from .models import Producto, Categoria

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()  # Esto guarda los datos en la base de datos
            return redirect('agregar_producto')  # Redirige a la misma página después de guardar
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def buscar_producto(request):
    # Ejemplo de lógica de búsqueda de productos (reemplaza esto con tu lógica real)
    productos = Producto.objects.all()  # Obtener todos los productos
    context = {'productos': productos}  # Definir el contexto con los productos
    return render(request, 'buscar_producto.html', context)
