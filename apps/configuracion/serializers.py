from rest_framework import serializers
from ..configuracion.models import ConfiguracionRestaurante

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionRestaurante
        fields = '__all__'
