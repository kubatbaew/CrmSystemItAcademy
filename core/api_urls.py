from django.urls import path, include


urlpatterns = [
    path('', include('apps.directions.urls')),
    path('', include('apps.groups.urls')),
    path('', include('apps.students.urls')),
]
