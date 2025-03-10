# Generated by Django 4.2.6 on 2023-12-01 01:10

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_task_is_archived_alter_task_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='points',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.datetime(2023, 12, 1, 1, 10, 47, 32944, tzinfo=datetime.timezone.utc))]),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
