from apps.students import serializers

from rest_framework import viewsets, response, decorators, mixins

from apps.students.models import Student
from apps.groups.models import Group
from apps.schedules.serializers import LessonSerializerForStudent


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
        group = student.group

        print(group)

        serializer = serializers.GroupSerializer(data=group.__dict__, instance=group)
        serializer.is_valid(raise_exception=True)
        
        return response.Response(data=serializer.data, status=200)
    

    @decorators.action(detail=True, methods=['GET'], url_path="schedules")
    def all_schedules(self, request, pk=None):
        student = self.get_object()
        schedules = student.group.schedule.lessons.all()
        print(schedules)

        serializer = LessonSerializerForStudent(data=[i.__dict__ for i in schedules], many=True)
        serializer.is_valid(raise_exception=True)

        return response.Response(data=serializer.data, status=200)


class StudentProfileAPIViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get_queryset(self):
        student = Student.objects.get(username=self.request.user.username)
        return [student]
