# Generated by Django 5.0.4 on 2024-04-13 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0002_alter_group_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='Дата занятий')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='groups.group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
            },
        ),
    ]
