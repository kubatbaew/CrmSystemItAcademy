from apps.students import serializers

from rest_framework import viewsets, response, decorators

from apps.students.models import Student
from apps.groups.models import Group


class StudentAPIViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.StudentCreateSerializer
        return self.serializer_class

    @decorators.action(detail=True, methods=['GET'], url_path="group")
    def students_groups(self, request, pk=None):
        student = self.get_object()
        group = Group.objects.get(id=student.group.id)

        serializer = serializers.GroupSerializer(data=group.__dict__, instance=group)
        serializer.is_valid(raise_exception=True)
        
        return response.Response(data=serializer.data, status=200)
