from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Especialidad_medica(models.Model):
    descripcion = models.CharField(max_length=50)
    codigo_cartilla = models.IntegerField(primary_key=True)

class Datos_profesional(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Sedes(models.Model):
    direccion = models.CharField(max_length=40)
    numero = models.IntegerField()

class Solicitante(models.Model):
    nombre_completo= models.CharField(max_length=80)
    email = models.EmailField()    