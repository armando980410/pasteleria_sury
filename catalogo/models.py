from django.db import models

# Create your models here.

class imagen(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=64)
    imagen = models.TextField()
    descripcion = models.TextField()
    precio = models.FloatField(default=0)
    activo = models.BooleanField()
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural='Imagenes'
