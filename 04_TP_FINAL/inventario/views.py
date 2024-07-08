from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# View personalizada de login
class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True  # Redirige a la página principal si el usuario ya está autenticado

    def get_success_url(self):
        return '/productos/'


# TODO: CRUD PRODUCTOS
@login_required
def listado_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'productos.html', {'productos': productos, 'categorias': categorias})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        stock = request.POST.get("stock")
        categoria_id = request.POST.get("categoria_id")
        fecha_vencimiento = request.POST.get("fecha_vencimiento")

        if not categoria_id:
            return render(request, 'crear_producto.html', {
                'error': 'La categoría es requerida.',
                'categorias': Categoria.objects.all()
            })

        categoria = Categoria.objects.get(id=categoria_id)
        
        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
            fecha_vencimiento=fecha_vencimiento if fecha_vencimiento else None
        )
        producto.save()
        return redirect('listado_productos')  # Redirige al listado de productos
    return render(request, 'crear_producto.html', {
        'categorias': Categoria.objects.all()
    })

@login_required
def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    categorias = Categoria.objects.all()
    return render(request, 'editar_producto.html', {'producto': producto, 'categorias': categorias})

@login_required
def update_producto(request, id):
    producto = Producto.objects.get(id=id)
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    precio = request.POST["precio"]
    stock = request.POST["stock"]
    categoria_id = request.POST["categoria_id"]
    categoria = Categoria.objects.get(id=categoria_id)
    fecha_vencimiento = request.POST["fecha_vencimiento"]
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.stock = stock
    producto.categoria = categoria
    producto.fecha_vencimiento = fecha_vencimiento if fecha_vencimiento else None
    producto.save()
    return redirect('listado_productos')  # Redirige al listado de productos

@login_required
def delete_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('listado_productos')  # Redirige al listado de productos


# TODO: CRUD CATEGORIA

@login_required
def detalle_categoria(request, id):
    productos = Producto.objects.filter(categoria__id=id)
    return render(request, 'productos.html', {'productos': productos})
