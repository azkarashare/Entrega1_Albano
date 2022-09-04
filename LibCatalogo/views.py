from django.shortcuts import render

from .forms import *
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
    return render(request, "LibCatalogo/usuarios.html")

#Vistas para formularios

def libros_f(request):
    if request.method=="POST":
        form_l=LibrosForm(request.POST)
        #print(form_l)
        if form_l.is_valid():
            nuevo_libro_data=form_l.cleaned_data
            #print(nuevo_libro_data)
            titulo=nuevo_libro_data["titulo"]
            genero=nuevo_libro_data["genero"]
            autor=nuevo_libro_data["autor"]
            sumario=nuevo_libro_data["sumario"]
            idioma=nuevo_libro_data["idioma"]
            nuevo_libro=Libros(titulo=titulo, genero=genero, autor=autor, sumario=sumario, idioma=idioma)
            nuevo_libro.save()
            return render(request, "LibCatalogo/cargaexito.html", {"mensaje":"Libro creado de forma exitosa!"})       
    else:
        l_formulario=LibrosForm()
        return render(request, "LibCatalogo/libros_f.html", {"l_formulario":l_formulario})

def autores_f(request):
    if request.method=="POST":
        form_a=AutoresForm(request.POST)
        if form_a.is_valid():
            nuevo_autor_data=form_a.cleaned_data
            nombre=nuevo_autor_data["nombre"]
            apellido=nuevo_autor_data["apellido"]
            fecha_n=nuevo_autor_data["fecha_n"]
            fecha_d=nuevo_autor_data["fecha_d"]
            nuevo_autor=Autores(nombre=nombre, apellido=apellido, fecha_n=fecha_n, fecha_d=fecha_d)
            nuevo_autor.save()
            return render(request, "LibCatalogo/cargaexito.html", {"mensaje":"Autor creado de forma exitosa!"})       
    else:
        a_formulario=AutoresForm()
        return render(request, "LibCatalogo/autores_f.html", {"a_formulario":a_formulario})

def generos_f(request):
    if request.method=="POST":
        form_g=GeneroForm(request.POST)
        if form_g.is_valid():
            nuevo_genero_data=form_g.cleaned_data
            nombre_g=nuevo_genero_data["nombre_g"]
            nuevo_genero=Genero(nombre_g=nombre_g)
            nuevo_genero.save()
            return render(request, "LibCatalogo/cargaexito.html", {"mensaje":"Genero creado de forma exitosa!"})       
    else:
        g_formulario=GeneroForm()
        return render(request, "LibCatalogo/generos_f.html", {"g_formulario":g_formulario})
