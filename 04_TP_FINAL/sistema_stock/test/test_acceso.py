import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

from inventario.models import Producto

# Fixtures
@pytest.fixture
def admin_user():
    """Crear un usuario admin para pruebas."""
    User = get_user_model()
    return User.objects.create_superuser(username='admin_ub', password='ub_test2024')

# Pruebas
@pytest.mark.django_db
def test_acceso(admin_user, client):
    """ID DE CASO: 1 - Verificar acceso al sistema."""
    client.login(username='admin_ub', password='ub_test2024')
    response = client.get(reverse('listado_productos'))
    assert response.status_code == 200
    assert 'Productos' in response.content.decode()




# @pytest.fixture
# def categoria():
#     """Crear una categoría para pruebas."""
#     return Categoria.objects.create(nombre='Almacén')

@pytest.fixture
def producto(categoria):
    """Crear un producto para pruebas."""
    return Producto.objects.create(
        nombre='Arroz',
        descripcion='Arroz Integral',
        precio=100,
        stock=10,
        categoria=categoria,
        fecha_vencimiento='2025-12-06'
    )



# @pytest.mark.django_db
# def test_agregar_producto(admin_user, client, categoria):
#     """ID DE CASO: 2 - Verificar creación de un nuevo producto."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.post(reverse('crear_producto'), {
#         'nombre': 'Nuevo Producto',
#         'descripcion': 'Descripción del nuevo producto',
#         'precio': 150,
#         'stock': 20,
#         'categoria': categoria.id,
#         'fecha_vencimiento': '2025-12-31'
#     })
#     assert response.status_code == 302  # Redirección a la lista de productos
#     assert Producto.objects.filter(nombre='Nuevo Producto').exists()

# @pytest.mark.django_db
# def test_agregar_producto_nombre_vacio(admin_user, client, categoria):
#     """ID DE CASO: 3 - Crear un nuevo producto con nombre vacío."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.post(reverse('crear_producto'), {
#         'nombre': '',
#         'descripcion': 'Descripción con nombre vacío',
#         'precio': 50,
#         'stock': 20,
#         'categoria': categoria.id,
#         'fecha_vencimiento': '2025-12-31'
#     })
#     assert response.status_code == 200
#     assert 'Este campo es obligatorio.' in response.content.decode()

# @pytest.mark.django_db
# def test_agregar_producto_precio_negativo(admin_user, client, categoria):
#     """ID DE CASO: 4 - Crear un nuevo producto con precio negativo."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.post(reverse('crear_producto'), {
#         'nombre': 'Harina',
#         'descripcion': 'Harina de Trigo',
#         'precio': -150,
#         'stock': 5,
#         'categoria': categoria.id,
#         'fecha_vencimiento': '2024-11-10'
#     })
#     assert response.status_code == 200
#     assert 'Asegúrese de que este valor sea mayor o igual a 0.' in response.content.decode()

# @pytest.mark.django_db
# def test_agregar_producto_categoria_vacia(admin_user, client):
#     """ID DE CASO: 5 - Crear un nuevo producto sin seleccionar categoría."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.post(reverse('crear_producto'), {
#         'nombre': 'Harina',
#         'descripcion': 'Harina Integral',
#         'precio': 150,
#         'stock': 5,
#         'categoria': '',
#         'fecha_vencimiento': '2024-11-10'
#     })
#     assert response.status_code == 200
#     assert 'Este campo es obligatorio.' in response.content.decode()

# @pytest.mark.django_db
# def test_agregar_producto_campos_vacios(admin_user, client):
#     """ID DE CASO: 6 - Crear un producto con todos los campos vacíos."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.post(reverse('crear_producto'), {})
#     assert response.status_code == 200
#     assert 'Este campo es obligatorio.' in response.content.decode()

# @pytest.mark.django_db
# def test_agregar_producto_campos_maximo(admin_user, client, categoria):
#     """ID DE CASO: 7 - Crear un producto con todos los campos al máximo."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.post(reverse('crear_producto'), {
#         'nombre': 'x' * 255,
#         'descripcion': 'x' * 255,
#         'precio': 999999.99,
#         'stock': 1000000,
#         'categoria': categoria.id,
#         'fecha_vencimiento': '2024-11-10'
#     })
#     assert response.status_code == 302  # Redirección a la lista de productos
#     assert Producto.objects.filter(nombre='x' * 255).exists()

# @pytest.mark.django_db
# def test_visualizar_detalle_producto(admin_user, client, producto):
#     """ID DE CASO: 8 - Visualizar detalles de un producto."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.get(reverse('detalle_producto', args=[producto.id]))
#     assert response.status_code == 200
#     assert 'Arroz Integral' in response.content.decode()

# @pytest.mark.django_db
# def test_editar_producto(admin_user, client, producto):
#     """ID DE CASO: 9 - Editar un producto existente."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.post(reverse('editar_producto', args=[producto.id]), {
#         'nombre': 'Harina',
#         'descripcion': 'Harina Integral',
#         'precio': 250,
#         'stock': 5,
#         'categoria': producto.categoria.id,
#         'fecha_vencimiento': '2024-11-10'
#     })
#     assert response.status_code == 302  # Redirección a la lista de productos
#     producto.refresh_from_db()
#     assert producto.precio == 250

# @pytest.mark.django_db
# def test_editar_precio_producto(admin_user, client, producto):
#     """ID DE CASO: 10 - Actualizar el precio de un producto y verificar."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.post(reverse('editar_producto', args=[producto.id]), {
#         'nombre': producto.nombre,
#         'descripcion': producto.descripcion,
#         'precio': 400,
#         'stock': producto.stock,
#         'categoria': producto.categoria.id,
#         'fecha_vencimiento': producto.fecha_vencimiento
#     })
#     assert response.status_code == 302  # Redirección a la lista de productos
#     producto.refresh_from_db()
#     assert producto.precio == 400

# @pytest.mark.django_db
# def test_eliminar_producto(admin_user, client, producto):
#     """ID DE CASO: 11 - Eliminar un producto."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.post(reverse('eliminar_producto', args=[producto.id]), follow=True)
#     assert response.status_code == 200
#     assert not Producto.objects.filter(id=producto.id).exists()

# @pytest.mark.django_db
# def test_confirmacion_eliminar_producto(admin_user, client, producto):
#     """ID DE CASO: 12 - Verificar mensaje de confirmación antes de eliminar."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.get(reverse('eliminar_producto', args=[producto.id]))
#     assert response.status_code == 200
#     assert '¿Estás seguro de que deseas eliminar este producto?' in response.content.decode()

# @pytest.mark.django_db
# def test_validacion_campos_crear_producto(admin_user, client, categoria):
#     """ID DE CASO: 13 - Verificar validación de campos al crear producto."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.post(reverse('crear_producto'), {
#         'nombre': '',
#         'descripcion': '',
#         'precio': '',
#         'stock': '',
#         'categoria': '',
#         'fecha_vencimiento': ''
#     })
#     assert response.status_code == 200
#     assert 'Este campo es obligatorio.' in response.content.decode()

# @pytest.mark.django_db
# def test_buscar_producto_por_nombre(admin_user, client, producto):
#     """ID DE CASO: 14 - Buscar un producto por nombre."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.get(reverse('listado_productos') + '?search=Arroz')
#     assert response.status_code == 200
#     assert 'Arroz Integral' in response.content.decode()

# @pytest.mark.django_db
# def test_formato_fecha_vencimiento(admin_user, client):
#     """ID DE CASO: 15 - Comprobar formato de fecha en productos."""
#     client.login(username='admin_ub', password='ub_test2024')
#     response = client.post(reverse('crear_producto'), {
#         'nombre': 'Producto',
#         'descripcion': 'Descripción',
#         'precio': 50,
#         'stock': 10,
#         'categoria': Categoria.objects.first().id,
#         'fecha_vencimiento': '2024-07-05'
#     })
#     assert response.status_code == 302
#     producto = Producto.objects.get(nombre='Producto')
#     fecha_vencimiento = parse_date(producto.fecha_vencimiento)
#     assert fecha_vencimiento.strftime('%m-%d-%Y') == '07-05-2024'
