from rest_framework import serializers, validators

from apps.students.models import Student
from apps.groups.models import Group
from apps.mentors.models import Mentor


class StudentSerializer(serializers.ModelSerializer):
    """ Студент Сериализатор """
    direction = serializers.CharField()

    class Meta:
        model = Student
        fields = [
            'id',
            'group',
            'direction',
            'username',
            'email',
            'full_name',
            'phone_number',
        ]


class StudentCreateSerializer(serializers.ModelSerializer):
    """ Создание Студента Сериализатор """
    password = serializers.CharField(
        write_only=True,
        required=False
    )
    class Meta:
        model = Student
        fields = [
            'username',
            'full_name',
            'group',
            'direction',
            'phone_number',
            'email',
            'password',
        ]

    def create(self, validated_data):
        password = validated_data['password']

        if not password:
            raise ValueError("Ошибка. Нет пароля")
        
        student = Student(**validated_data)
        student.set_password(password)
        student.save()

        return student
    
    def validate_phone_number(self, value):
        if '+996' not in value:
            raise validators.ValidationError("[!]Ошибка: Номер телефона неправильный!")
        if len(value) != 13:
            raise validators.ValidationError("[!]Ошибка: Длина не совпадает")
        return value


class MentorSerializer(serializers.ModelSerializer):
    direction = serializers.CharField()
    
    class Meta:
        model = Mentor
        fields = [
            'id',
            'full_name',
            'direction',
            'age',
            'experience',
        ]


class GroupSerializer(serializers.ModelSerializer):
    """ Группа Сериализатор """
    students = StudentSerializer(many=True, read_only=True)
    mentor = MentorSerializer(read_only=True)
    direction = serializers.CharField()

    class Meta:
        model = Group
        fields = [
            'id',
            'title',
            'direction',
            'created_at',
            'mentor',
            'students',
        ]
