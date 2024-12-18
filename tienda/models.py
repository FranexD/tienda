from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', default='productos/default_image.jpg')

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    comentario = models.TextField()

    def __str__(self):
        return self.nombre
