from django.db import models

#TODO: Creamos las entidades del proyecto
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria_id = models.IntegerField()
    fecha_vencimiento = models.DateField()
    fecha_alta = models.DateField()
    fecha_baja = models.DateField(null=True)
    
    def __str__(self):
        return self.nombre