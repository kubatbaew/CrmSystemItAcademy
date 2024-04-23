from rest_framework import viewsets

from apps.payments.serializers import PaymentSerializer
from apps.payments.models import Payment


class PaymentAPIViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
