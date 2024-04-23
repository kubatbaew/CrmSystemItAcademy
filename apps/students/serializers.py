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


class StudentChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = [
            'old_password',
            'new_password',
            're_password',
        ]
    
    def update(self, instance, validated_data):
        new_password = validated_data.get('new_password')

        instance.set_password(new_password)
        instance.save()

        return instance
    
    def validate(self, attrs):
        new_password = attrs.get("new_password")
        re_password = attrs.get("re_password")

        if new_password != re_password:
            raise serializers.ValidationError("Пароли не совпадают")

        return attrs
    
    def validate_old_password(self, value):
        student = self.instance
        if not student.check_password(value):
            raise serializers.ValidationError("Старый пароль не правильный")
        
        return value

    def save(self):
        student = self.instance
        new_password = self.validated_data['new_password']

        student.set_password(new_password)
        student.save()

        return student
    

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

