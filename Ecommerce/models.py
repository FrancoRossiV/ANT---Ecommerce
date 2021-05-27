from django.db import models

# Create your models here.


# Hacer desp clase de categoria probablemente


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12, default="Sin Numero")

    def __str__(self):
        return " " + str(self.nombre)     


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    status_categoria=[
    ('Jardin', 'Jardin'),
    ('Cocina', 'Cocina'),
    ('Habitacion', 'Habitacion'),
    ('Baño', 'Baño'),
    ]
    categoria = models.CharField(max_length=50, choices=status_categoria, default=None)
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)

    def __str__(self):
        return " " + str(self.nombre)    


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12, default="Sin Numero")
    mail = models.EmailField(max_length=100)

    def __str__(self):
        return " " + str(self.nombre) 

class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto, default = None)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return " " + str(self.cliente) 

class Venta(models.Model):
    carrito = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    status_pago=[
    ('Transferencia', 'Transferencia'),
    ('Credito', 'Credito'),
    ('Debito', 'Debito'),
    ]
    metodo_pago = models.CharField(max_length=50, choices=status_pago, default=None)
    fecha = models.DateField() 


