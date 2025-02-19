# Generated by Django 5.1.6 on 2025-02-17 05:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.CharField(max_length=100)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('unique_visitors', models.IntegerField()),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
