from django.db import models
import uuid


# Create your models here.

class Libros(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid1, help_text="ID único de este ejemplar")
    titulo=models.CharField(max_length=50)
    genero=models.CharField(max_length=30)
    autor=models.CharField(max_length=50)
    sumario=models.TextField(max_length=120)
    idioma=models.CharField(max_length=50)

class Autores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_n=models.DateField(null=True, blank=True)
    fecha_d=models.DateField('Fallecido', null=True, blank=True)

class Genero(models.Model):
    nombre_g=models.CharField(max_length=50)

class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    alias=models.CharField(max_length=50)
    correo=models.EmailField()
    contrasenia=models.CharField(max_length=50)




