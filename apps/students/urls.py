from rest_framework import routers

from apps.students.views import StudentAPIViewSet


router = routers.DefaultRouter()

router.register('students', StudentAPIViewSet)


urlpatterns = router.urls
