from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', include('apps.payments.urls')),
    path('', include('apps.mentors.urls')),
    path('', include('apps.directions.urls')),
    path('', include('apps.groups.urls')),
    path('', include('apps.students.urls')),
    path('token_create/', TokenObtainPairView.as_view()),
    path('token_refresh/', TokenRefreshView.as_view())
]
