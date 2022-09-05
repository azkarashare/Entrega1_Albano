"""Libreria_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from LibCatalogo.views import *


urlpatterns = [
    path('libros/', libros, name='libros'),
    path('autores/', autores, name='autores'),
    path('generos/', generos, name='generos'),
    path('usuarios/', usuario, name='usuarios'),
    path('', inicio, name='inicio'),
    #path('inicio/', inicio, name='inicio'),
    path('librosf/', libros_f, name='librosf'),
    path('autoresf/', autores_f, name='autoresf'),
    path('generosf/', generos_f, name='generosf'),
    #Urls de busquedas
    path('buscar_l_by_t/', f_busqueda_lib_by_title, name='buscar_l_by_t'),
    path('result_l_by_t/', f_resultado_lib_by_title, name='result_l_by_t'),
]