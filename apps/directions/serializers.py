from rest_framework import serializers

from apps.directions.models import Direction


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = [
            'id',
            'title',
            'created_at',
        ]
