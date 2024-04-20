from django.db import models

from apps.users.models import User
from apps.directions.models import Direction


class Mentor(User):
    direction = models.ForeignKey(
        Direction, on_delete=models.SET_NULL,
        related_name="mentors",
        verbose_name="Направление",
        null=True,
    )
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
