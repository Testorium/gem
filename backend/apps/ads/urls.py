from rest_framework.routers import DefaultRouter

from .views import AdViewSet

router = DefaultRouter()
router.register(r"", AdViewSet)

urlpatterns = router.urls
