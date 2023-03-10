from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=['created_at', 'nombre', 'updated']
    list_display_links=['nombre',]
    list_filter=['status',]
