# Generated by Django 3.1.7 on 2021-05-02 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_main', '0006_task_completed_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='completed_date',
            new_name='complete_at',
        ),
    ]
