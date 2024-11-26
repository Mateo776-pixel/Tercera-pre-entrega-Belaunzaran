from django.db import models

# Create your models here.
class Expreso(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del expreso
    codigo = models.CharField(max_length=20, unique=True)  # Código único del expreso
    direccion_entrega = models.CharField(max_length=200)  # Dirección de entrega asociada

    def __str__(self):
        return f"{self.nombre} - {self.codigo}"

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)  # Nombre del vendedor
    apellido = models.CharField(max_length=50)  # Apellido del vendedor
    codigo = models.CharField(max_length=20, unique=True)  # Código único del vendedor

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.codigo}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15) 
    direccion = models.CharField(max_length=255)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)