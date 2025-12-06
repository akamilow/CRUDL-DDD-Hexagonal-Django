# Modelo Django ORM. Implementa la persistencia, desacoplado del dominio.
from django.db import models

class UserModel(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10)
    password_hash = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"
