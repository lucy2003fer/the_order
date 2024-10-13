from rest_framework import serializers
from .models import Pedido
from .serializers import DetalleSerializer

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetalleSerializer(many=True, read_only=True)  # Mostrar los detalles del pedido

    class Meta:
        model = Pedido
        fields = '__all__'
