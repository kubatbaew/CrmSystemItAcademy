from rest_framework import serializers

from apps.payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = Payment
        fields = [
            'id',
            'date_of_payment',
            'file',
        ]

class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'student',
            'file',
            'date_of_payment',
        ]
        read_only_fields = [
            'student',
        ]
        