from django.db import models
from django.urls import reverse
# Create your models here.

class modeloMascota(models.Model):
    Nombre = models.CharField(max_length=100)
    NombreCliente = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=100)
