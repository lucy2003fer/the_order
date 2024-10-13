from rest_framework.routers import DefaultRouter
from .views import ConfiguracionViewSet

router = DefaultRouter()
router.register(r'Configuracion', ConfiguracionViewSet)

urlpatterns = router.urls
