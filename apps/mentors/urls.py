from rest_framework.routers import DefaultRouter

from apps.mentors.views import MentorAPIViewSet

router = DefaultRouter()

router.register('mentors', MentorAPIViewSet)

urlpatterns = router.urls
