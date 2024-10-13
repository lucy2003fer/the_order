from rest_framework import serializers
from .models import ConfiguracionRestaurante

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionRestaurante
        fields = '__all__'
