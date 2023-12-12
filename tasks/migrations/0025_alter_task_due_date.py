# Generated by Django 4.2.6 on 2023-12-08 13:28

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0024_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.datetime(2023, 12, 8, 13, 28, 37, 141497, tzinfo=datetime.timezone.utc))]),
        ),
    ]
