# Generated by Django 3.2.19 on 2023-07-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_phonelog_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]