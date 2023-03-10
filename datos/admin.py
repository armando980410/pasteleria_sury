from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(info)
class InfoAdmin(admin.ModelAdmin):
    list_display_links=['nombre',]
    list_display=['created_at', 'nombre', 'cel', 'updated']
