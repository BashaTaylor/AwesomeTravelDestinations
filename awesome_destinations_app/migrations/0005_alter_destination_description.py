# Generated by Django 5.1 on 2024-09-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awesome_destinations_app', '0004_destination_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='description',
            field=models.TextField(default='Default description'),
        ),
    ]
