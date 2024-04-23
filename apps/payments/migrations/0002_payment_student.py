# Generated by Django 5.0.4 on 2024-04-23 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
        ('students', '0004_student_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='students.student', verbose_name='Студент'),
            preserve_default=False,
        ),
    ]
