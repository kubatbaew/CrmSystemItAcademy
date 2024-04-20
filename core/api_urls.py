from django.urls import path, include


urlpatterns = [
    path('', include('apps.groups.urls')),
    path('', include('apps.students.urls')),
]
