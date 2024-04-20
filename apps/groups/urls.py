from rest_framework.routers import DefaultRouter

from apps.groups.views import GroupAPIViewSet


router = DefaultRouter()

router.register('groups', GroupAPIViewSet)


urlpatterns = router.urls
