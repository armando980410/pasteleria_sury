from django.db import models

# Create your models here.

class producto(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=64)
    imagen = models.TextField()
    descripcion = models.TextField()
    precio = models.FloatField()
    costo = models.FloatField()
    status = models.BooleanField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
