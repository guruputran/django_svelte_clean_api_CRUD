# Generated by Django 4.0.4 on 2022-05-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_remove_todo_body_todo_iscompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
