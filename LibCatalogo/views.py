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

#-----VISTA PARA FORMULARIOS DE BUSQUEDA-----

#Esta es la del formulario de busqueda
def f_busqueda_lib_by_title(request):
    return render(request, "LibCatalogo/busquedas/busq_lib_by_title.html")

def f_busqueda_lib_by_gen(request):
    return render(request, "LibCatalogo/busquedas/busq_lib_by_genero.html")

def f_busqueda_lib_by_autor(request):
    return render(request, "LibCatalogo/busquedas/busq_lib_by_autor.html")

#Esta es la que me muestra los resultados de titulos buscando por titulo
def f_resultado_lib_by_title(request):
    lib_by_title_v=request.POST["lib_by_title"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    titulo_libro_v=Libros.objects.filter(titulo__icontains=lib_by_title_v)
    return render(request, "LibCatalogo/busquedas/resultado_busq_lib_by_title.html", {"titulo_libro_k":titulo_libro_v})

#Esta es la que me muestra los resultados de titulos buscando por genero
def f_resultado_lib_by_gen(request):
    lib_by_gen_v=request.POST["lib_by_genero"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    titulo_libro_v=Libros.objects.filter(genero__icontains=lib_by_gen_v)
    return render(request, "LibCatalogo/busquedas/resultado_busq_lib_by_gen.html", {"titulo_libro_k":titulo_libro_v})

#Esta es la que me muestra los resultados de titulos buscando por autor
def f_resultado_lib_by_autor(request):
    lib_by_autor_v=request.POST["lib_by_autor"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    titulo_libro_v=Libros.objects.filter(autor__icontains=lib_by_autor_v)
    return render(request, "LibCatalogo/busquedas/resultado_busq_lib_by_title.html", {"titulo_libro_k":titulo_libro_v})
    



