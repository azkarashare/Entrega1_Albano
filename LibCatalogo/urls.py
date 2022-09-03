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
from LibCatalogo.views import autores, generos, inicio, libros, usuario

urlpatterns = [
    path('libros', libros, name='libros'),
    path('autores', autores, name='autores'),
    path('generos', generos, name='generos'),
    path('usuario', usuario),
    path('inicio', inicio),
]