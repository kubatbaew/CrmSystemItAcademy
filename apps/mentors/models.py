from django.db import models

from apps.users.models import User


class Mentor(User):
    full_name = models.CharField(
        max_length=120,
        verbose_name="Имя Ментора",
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="Возраст",
    )
    experience = models.PositiveSmallIntegerField(
        verbose_name="Опыт в разработке",
        help_text="Введите опыт в годах",
    )

    def get_mentor(self):
        return True

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Ментор"
        verbose_name_plural = "Менторы"
