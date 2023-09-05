from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
