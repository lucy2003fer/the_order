from rest_framework import serializers
from ..pedidos.models import Pedido
from ..detalles.serializers import DetalleSerializer

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetalleSerializer(many=True, read_only=True)  # Mostrar los detalles del pedido

    class Meta:
        model = Pedido
        fields = '__all__'
