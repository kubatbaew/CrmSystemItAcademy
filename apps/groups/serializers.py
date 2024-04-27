from rest_framework import serializers

from apps.groups.models import Group
from apps.students.serializers import StudentSerializer, MentorForStudentSerializer


class GroupSerializer(serializers.ModelSerializer):
    students = StudentSerializer(read_only=True, many=True)
    mentor = MentorForStudentSerializer()
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


class GroupListSerializer(serializers.ModelSerializer):
    direction = serializers.CharField()
    class Meta:
        model = Group
        fields = [
            'id',
            'direction',
            'title',
        ]


class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'title',
            'direction',
            'mentor',
        ]
