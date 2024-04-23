from rest_framework import serializers

from apps.mentors.models import Mentor


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = [
            'id',
            'username',
            'direction',
            'full_name',
            'age',
            'experience',
        ]


class MentorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = [
            'id',
            'username',
            'direction',
            'full_name',
            'age',
            'experience',
            'mentor_groups',
        ]


class MentorCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Mentor
        fields = [
            'id',
            'username',
            'direction',
            'full_name',
            'age',
            'experience',
            'password',
        ]
    
    def create(self, validated_data):
        password = validated_data['password']

        if not password:
            raise ValueError("Ошибка. Нет пароля")
        
        mentor = Mentor(**validated_data)
        mentor.set_password(password)
        mentor.save()

        return mentor
    
    def update(self, instance, validated_data):
        mentor = instance
        password = validated_data.get('password')

        if not password:
            raise serializers.ValidationError("Пароль отсутстует")
        
        mentor.set_password(password)
        mentor.save()

        return mentor
