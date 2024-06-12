from django.db import models
from django.utils import timezone

#TODO: Creamos las entidades del proyecto

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.IntegerField()
    fecha_vencimiento = models.DateField(null=True, blank=True)
    fecha_alta = models.DateField(default=timezone.now, blank=True)
    fecha_baja = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre