# Generated by Django 3.2.19 on 2023-07-02 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20230702_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
