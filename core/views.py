from django.shortcuts import render

from catalogo.models import *
from datos.models import *
from productos.models import *

# Create your views here.

def Index(request):
    datos = info.objects.all()
    productos = producto.objects.filter(status=True)
    imagenes = imagen.objects.filter(activo=True)
    context = {
        'datos':datos,
        'productos':productos,
        'imagenes':imagenes,
    }
    
    return render(request, 'front/index.html', context)

def Product_Detail(request, pk):
    query = producto.objects.get(pk=pk)
    context = {
        'body':query,
    }
    return render(request, 'front/detail.html', context)

def Imagen_Detail(request, pk):
    query = imagen.objects.get(pk=pk)
    context = {
        'body':query,
    }
    return render(request, 'front/detail.html', context)
