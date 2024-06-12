from django.urls import path
from .views import *

urlpatterns = [
    path('',listado_productos, name='listado_productos'),
    path('crear/', crear_producto, name='crear_producto'),
    path('editar/<id>', editar_producto, name = 'editar_producto'),
    path('actualizar/<id>', update_producto, name = 'actualizar_producto'),
    path('eliminar/<id>', delete_producto, name = 'eliminar_producto'),

]