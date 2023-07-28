from django.db import models

# Create your models here.

class Curso(models.Model):
    #Atributos = columna de una base de datos
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()
    
class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(blank=True)

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entregable = models.DateField(auto_now_add=True)
    esta_aprobado = models.BooleanField(default=False)

