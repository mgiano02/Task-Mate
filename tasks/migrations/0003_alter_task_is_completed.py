# Generated by Django 4.1.7 on 2023-03-07 03:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_remove_task_state_date_task_start_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
    ]