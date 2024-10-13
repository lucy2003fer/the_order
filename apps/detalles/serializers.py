from rest_framework import serializers
from .models import DetallePedido

class DetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'
