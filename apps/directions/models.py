from django.db import models


class Direction(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name="Название",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"
