# Generated by Django 5.1 on 2024-09-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravelDestinations_app', '0003_alter_destination_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='description',
            field=models.TextField(default='default description'),
            preserve_default=False,
        ),
    ]
