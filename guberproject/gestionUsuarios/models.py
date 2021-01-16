from django.db import models

class cocina_iot(models.Model):
    id_sincronizacion = models.CharField(max_length=30)


class chef(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    tarjeta_profesiona = models.CharField(max_length=30)
    correo = models.EmailField()
    direccion = models.CharField(max_length=50)
    user = models.CharField(max_length=30)
    pw = models.CharField(max_length=30)
    id_cocina_iot = models.ForeignKey(cocina_iot, default=1, on_delete=models.CASCADE)

class receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    precio = models.IntegerField()

class chef_receta(models.Model):
    estado = models.CharField(max_length=20)
    id_chef = models.ForeignKey(chef,on_delete=models.CASCADE)
    id_receta = models.ForeignKey(receta, on_delete=models.CASCADE)

class cliente(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    correo = models.EmailField()
    direccion = models.CharField(max_length=50)
    user = models.CharField(max_length=30)
    pw = models.CharField(max_length=30)

class caja_iot(models.Model):
    id_sincronizacion = models.CharField(max_length=30)

class domiciliario(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    tarjeta_profesiona = models.CharField(max_length=30)
    correo = models.EmailField()
    direccion = models.CharField(max_length=50)
    user = models.CharField(max_length=30)
    pw = models.CharField(max_length=30)
    id_caja_iot = models.ForeignKey(caja_iot, default=1,on_delete=models.CASCADE)

class pedidos(models.Model):
    direccion_entrega = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=1000)
    propina = models.IntegerField()
    forma_pago = models.CharField(max_length=20)
    total = models.IntegerField()
    fecha_pedido = models.TimeField()
    id_chef_recetas = models.ForeignKey(chef_receta, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    id_domiciliario = models.ForeignKey(domiciliario, on_delete=models.CASCADE)


