from rest_framework import serializers

from apps.groups.models import Group
from apps.students.serializers import StudentSerializer, MentorSerializer


class GroupSerializer(serializers.ModelSerializer):
    students = StudentSerializer(read_only=True, many=True)
    mentor = MentorSerializer()
    class Meta:
        model = Group
        fields = [
            'id',
            'title',
            'created_at',
            'mentor',
            'students',
        ]


class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'title',
        ]


class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'title',
            'mentor',
        ]
