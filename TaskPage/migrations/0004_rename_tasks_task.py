# Generated by Django 5.0.6 on 2024-05-21 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskPage', '0003_alter_tasks_createdby'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]
