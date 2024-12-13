# Generated by Django 5.1.1 on 2024-12-10 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('agency_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('agency_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('stop_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('stop_name', models.CharField(max_length=100)),
                ('stop_location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('route_long_name', models.CharField(max_length=100)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideshare.agency')),
            ],
            options={
                'verbose_name': 'Route',
                'verbose_name_plural': 'Routes',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideshare.route')),
            ],
        ),
        migrations.CreateModel(
            name='StopTimes',
            fields=[
                ('stop_time_id', models.AutoField(primary_key=True, serialize=False)),
                ('arrival_time', models.TimeField(blank=True, null=True)),
                ('departure_time', models.TimeField(blank=True, null=True)),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideshare.stop')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideshare.trip')),
            ],
        ),
    ]
