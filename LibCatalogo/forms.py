#from socket import fromshare
from django import forms
import uuid

class LibrosForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    sumario = forms.CharField(max_length=250)
    idioma = forms.CharField(max_length=50)

    #def __str__(self):
    #    return self.titulo+" "+self.genero

class AutoresForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    fecha_n = forms.DateField()
    fecha_d = forms.DateField()

class GeneroForm(forms.Form):
    nombre_g = forms.CharField(max_length=50)