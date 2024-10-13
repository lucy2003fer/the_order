from django.db import models

# Create your models here.

class Pedido(models.Model):
    ESTADOS = [
        ('EN_ESPERA', 'En espera'),
        ('EN_PREPARACION', 'En preparación'),
        ('PREPARADO', 'Preparado'),
    ]
    cliente = models.CharField(max_length=100)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='EN_ESPERA')

    def __str__(self):
        return f"Pedido de {self.cliente} ({self.estado})"

