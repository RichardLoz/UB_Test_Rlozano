from django.contrib import admin
from django.urls import path, include
from inventario.views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', CustomLoginView.as_view(), name='login'),  # La página principal debe ser el login
    path('productos/', include('inventario.urls')),  # Rutas para productos
]