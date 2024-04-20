from django.db import models

from apps.users.models import User

from apps.groups.models import Group
from apps.directions.models import Direction


class Student(User):
    direction = models.ForeignKey(
        Direction, on_delete=models.SET_NULL,
        related_name="students",
        verbose_name="Направление",
        null=True,
    )
    group = models.ForeignKey(
        Group, 
        on_delete=models.SET_NULL,
        related_name="students",
        verbose_name="Группа",
        null=True, blank=True,
    )
    full_name = models.CharField(
        max_length=50,
        verbose_name="Полное имя",
    )
    phone_number = models.CharField(
        max_length=16,
        verbose_name="Номер телефона",
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
