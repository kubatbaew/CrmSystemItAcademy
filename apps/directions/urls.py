from rest_framework.routers import DefaultRouter

from apps.directions.views import DirectionAPIViewSet


router = DefaultRouter()

router.register("directions", DirectionAPIViewSet)


urlpatterns = router.urls
