from django.db import models

# Create your models here.


class Clientes (models.Model):
    nombre=models.TextField(max_length=30)
    direcccion=models.CharField(max_length=30)
    email=models.EmailField()
    tfno=models.IntegerField(max_length=7)
    precios=models.IntegerField()

class  Articulos (models.Model):
    nombre=models.TextField(max_length=30)
    seccion=models.TextField(max_length=20)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
    

