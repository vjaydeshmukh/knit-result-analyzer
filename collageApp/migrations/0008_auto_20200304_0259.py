# Generated by Django 3.0.3 on 2020-03-03 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collageApp', '0007_auto_20200304_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='total_marks',
            field=models.FloatField(default=10.0),
        ),
    ]
