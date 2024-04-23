from django.db import models
from apps.students.models import Student

class Payment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Студент',
    )
    file = models.FileField(
        upload_to='payment_file',
        verbose_name='Квитанция',
    )
    date_of_payment = models.DateField(
        verbose_name='Дата оплаты',
    )

    def __str__(self):
        return f'{self.date_of_payment}'
    
    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
