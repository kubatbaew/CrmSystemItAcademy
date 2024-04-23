from rest_framework.routers import DefaultRouter

from apps.payments.views import PaymentAPIViewSet


router = DefaultRouter()
router.register('payments', PaymentAPIViewSet)

urlpatterns = router.urls
