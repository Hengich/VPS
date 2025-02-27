# Generated by Django 4.2.18 on 2025-01-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPS',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('cpu', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('hdd', models.IntegerField()),
                ('status', models.CharField(choices=[('started', 'Started'), ('blocked', 'Blocked'), ('stopped', 'Stopped')], default='stopped', max_length=10)),
            ],
        ),
    ]
