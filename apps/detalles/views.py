from rest_framework import viewsets
from .models import DetallePedido
from .serializers import DetallePedidoSerializer

# Create your views here.

class DetalleViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetalleSerializer
