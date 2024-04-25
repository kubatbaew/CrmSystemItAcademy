from rest_framework import filters

from rest_framework.viewsets import ModelViewSet
from rest_framework import response

from apps.directions.models import Direction
from apps.directions.serializers import DirectionSerializer

from apps.students.models import Student

from utils.permissions import IsManager


class DirectionAPIViewSet(ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [IsManager]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        try:
            student = Student.objects.get(username=self.request.user.username)
            if student.direction:
                return Direction.objects.filter(id=student.direction.id)
            
        except Student.DoesNotExist:
            return self.queryset

        