# Generated by Django 4.1.5 on 2023-02-03 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thedar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='checkin',
            field=models.TimeField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='checkout',
            field=models.TimeField(max_length=200),
        ),
    ]