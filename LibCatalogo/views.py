from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    #return HttpResponse("Inicio")
    return render(request, "LibCatalogo/inicio.html")

def libros(request):
    return render(request, "LibCatalogo/libros.html")

def autores(request):
    return render(request, "LibCatalogo/autores.html")

def generos(request):
    return render(request, "LibCatalogo/generos.html")

def usuario(request):
    return render(request, "LibCatalogo/usuario.html")