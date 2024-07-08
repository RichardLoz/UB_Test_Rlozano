from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_productos, name='listado_productos'),  # Página de listado de productos
    path('crear/', views.crear_producto, name='crear_producto'),  # Crear un nuevo producto
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),  # Editar un producto existente
    path('actualizar/<int:id>/', views.update_producto, name='actualizar_producto'),  # Actualizar un producto
    path('eliminar/<int:id>/', views.delete_producto, name='eliminar_producto'),  # Eliminar un producto
    path('categoria/<int:id>/', views.detalle_categoria, name='detalle_categoria'),  # Detalle de categoría
]
