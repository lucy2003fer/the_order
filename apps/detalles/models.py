from django.db import models
from apps.productos.models import Productos
from apps.pedidos.models import Pedido

# Create your models here.

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, name='detalles', on_delete=models.SET_NULL,null=True)
    producto = models.ForeignKey(Productos, on_delete=models.SET_NULL,null=True)
    cantidad = models.PositiveIntegerField()
    observaciones = models.TextField(blank=True, null=True)
    empaque = models.CharField(max_length=50, choices=[('LLEVAR', 'Para llevar'), ('COMER_AQUI', 'Para comer aquí')])

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} ({self.pedido.cliente})"
