from apps.students import serializers

from rest_framework import viewsets, response, decorators, mixins, permissions

from apps.students.models import Student
from apps.groups.models import Group
from apps.schedules.serializers import LessonSerializerForStudent

from apps.payments.serializers import PaymentCreateSerializer, PaymentSerializer
from apps.payments.models import Payment

from utils.permissions import IsManager, IsStudent


class StudentAPIViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsStudent()]
        return [IsManager()]


    def get_serializer_class(self):
        if self.action == 'change_password':
            return serializers.StudentChangePasswordSerializer
        if self.action in ['create']:
            return serializers.StudentCreateSerializer
        if self.action == 'add_payment':
            return PaymentCreateSerializer
        return self.serializer_class


    @decorators.action(detail=True, methods=['PATCH', 'PUT'], url_path="change_password")
    def change_password(self, request, pk=None):
        student = self.get_object()
        
        serializer = self.get_serializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return response.Response({"message": "Пароль успешно изменен!"})


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


    @decorators.action(detail=True, methods=['POST'], url_path="add_payment")
    def add_payment(self, request, pk=None):
        student = self.get_object()

        payment = Payment.objects.create(
            file=request.data.get('file'),
            date_of_payment=request.data.get('date_of_payment'),
            student=student,
        )
        print(request.data)

        return response.Response({"message": "Оплата успешно произведена"})


    @decorators.action(detail=True, methods=['GET'], url_path='all_payments')
    def all_payments(self, request, pk=None):
        student = self.get_object()

        serializer = PaymentSerializer(student.payments, many=True)

        return response.Response(serializer.data, status=200)
    

class StudentProfileAPIViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get_queryset(self):
        student = Student.objects.get(username=self.request.user.username)
        return [student]
