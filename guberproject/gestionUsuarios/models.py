from django.db import models

class chef(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    tarjeta_profesiona = models.CharField(max_length=30)
    correo = models.EmailField()
    direccion = models.CharField(max_length=50)
    user = models.CharField(max_length=30)
    pw = models.CharField(max_length=30)

class cliente(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    correo = models.EmailField()
    direccion = models.CharField(max_length=50)
    user = models.CharField(max_length=30)
    pw = models.CharField(max_length=30)

class domiciliario(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    tarjeta_profesiona = models.CharField(max_length=30)
    correo = models.EmailField()
    direccion = models.CharField(max_length=50)
    user = models.CharField(max_length=30)
    pw = models.CharField(max_length=30)