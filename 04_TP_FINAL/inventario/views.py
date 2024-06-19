from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Producto, Categoria


#TODO: CRUD PRODUCTOS

def listado_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'productos.html', {'productos': productos, 'categorias': categorias})

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
        return redirect('/')
    return render(request, 'crear_producto.html', {
        'categorias': Categoria.objects.all()
    })

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    categorias = Categoria.objects.all()
    return render(request, 'editar_producto.html', {'producto': producto,'categorias': categorias })

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
    return redirect('/')

def delete_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/')


#TODO: CRUD CATEGORIA

def detalle_categoria(request,id):
    #categoria = Categoria.objects.get(id=id)
    #productos = Producto.objects.all()
    #categoria_productos = Categoria.productos.all()
    #Filtro
    productos = Producto.objects.filter(categoria__id=id)
    
