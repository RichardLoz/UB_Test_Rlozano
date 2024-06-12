from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Producto

def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos':productos})

# def crear_producto(request):
#     nombre = request.POST["nombre"]
#     descripcion = request.POST["descripcion"]
#     precio = request.POST["precio"]
#     stock = request.POST["stock"]
#     categoria = request.POST["categoria"]
#     fecha_vencimiento = request.POST["fecha_vencimiento"]
#     fecha_alta = request.POST["fecha_alta"]
#     fecha_baja = request.POST["fecha_baja"]
#     producto = Producto(nombre=nombre,descripcion=descripcion,precio=precio,stock=stock,categoria=categoria,fecha_vencimiento=fecha_vencimiento,fecha_alta=fecha_alta,fecha_baja=fecha_baja)
#     producto.save()
#     return redirect('/inventario/')

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        stock = request.POST.get("stock")
        categoria = request.POST.get("categoria")
        fecha_vencimiento = request.POST.get("fecha_vencimiento")
        fecha_baja = request.POST.get("fecha_baja")
        
        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria,
            fecha_vencimiento=fecha_vencimiento if fecha_vencimiento else None,
            fecha_alta= timezone.now(),
            fecha_baja=fecha_baja if fecha_baja else None
        )
        producto.save()
        return redirect('/inventario/')
    return render(request, 'crear_producto.html')

# def editar_producto(request, id):
#     producto = Producto.objects.get(id = id)
#     return render(request, 'editar_producto.html', {'producto':producto})

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, 'editar_producto.html', {
        'producto': {
            'id': producto.id,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'precio': producto.precio,
            'stock': producto.stock,
            'categoria': producto.categoria,
            'fecha_vencimiento': producto.fecha_vencimiento.strftime('%Y-%m-%d') if producto.fecha_vencimiento else '',
            'fecha_alta': producto.fecha_alta.strftime('%Y-%m-%d') if producto.fecha_alta else '',
            'fecha_baja': producto.fecha_baja.strftime('%Y-%m-%d') if producto.fecha_baja else '',
        }
    })

def update_producto(request, id):
    producto = Producto.objects.get(id = id)
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    precio = request.POST["precio"]
    stock = request.POST["stock"]
    categoria = request.POST["categoria"]
    fecha_vencimiento = request.POST["fecha_vencimiento"]
    fecha_alta = request.POST["fecha_alta"]
    fecha_baja = request.POST["fecha_baja"]
    producto.nombre = nombre
    producto.descripcion = descripcion
    producto.precio = precio
    producto.stock = stock
    producto.categoria = categoria
    producto.fecha_vencimiento = fecha_vencimiento
    producto.fecha_alta = fecha_alta
    producto.fecha_baja = fecha_baja
    producto.save()
    return redirect('/inventario/')

def delete_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/inventario/')