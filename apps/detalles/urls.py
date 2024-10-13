from rest_framework.routers import DefaultRouter
from .views import DetallePedidoViewSet

router = DefaultRouter()
router.register(r'detalles', DetallePedidoViewSet)

urlpatterns = router.urls

