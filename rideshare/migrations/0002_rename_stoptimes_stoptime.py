# Generated by Django 5.1.1 on 2024-12-11 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StopTimes',
            new_name='StopTime',
        ),
    ]
