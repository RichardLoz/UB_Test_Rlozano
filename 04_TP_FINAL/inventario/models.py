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
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField() 
    fecha_vencimiento = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre