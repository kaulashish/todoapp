# Generated by Django 3.1.7 on 2021-05-02 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_main', '0007_auto_20210502_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete_at',
            new_name='completed_at',
        ),
    ]