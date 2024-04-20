from django.db import models

from apps.mentors.models import Mentor
from apps.directions.models import Direction


class Group(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name="Название группы",
    )
    direction = models.ForeignKey(
        Direction, on_delete=models.SET_NULL,
        related_name="groups",
        verbose_name="Направление",
        null=True,
    )
    mentor = models.ForeignKey(
        Mentor, on_delete=models.SET_NULL,
        related_name='mentor_groups',
        verbose_name="Ментор",
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
