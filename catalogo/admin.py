from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display=['created_at', 'nombre', 'activo', 'updated']
    list_display_links=['nombre',]
    list_filter=['activo',]
