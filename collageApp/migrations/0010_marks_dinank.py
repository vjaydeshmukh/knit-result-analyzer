# Generated by Django 3.0.3 on 2020-03-08 07:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collageApp', '0009_auto_20200304_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='dinank',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
