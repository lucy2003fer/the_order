from rest_framework import viewsets
from .models import ConfiguracionRestaurante
from .serializers import ConfiguracionSerializer

# Create your views here.

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = ConfiguracionRestaurante.objects.all()
    serializer_class = ConfiguracionSerializer
