from django.db import models

# Create your models here.

class info(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=64)
    logo = models.TextField()
    descripcion = models.TextField()
    slogan = models.TextField()
    fb = models.TextField()
    ubicacion = models.TextField()
    cel = models.CharField(max_length=12)
    formulario = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural='Informacion'
