# Generated by Django 5.1.6 on 2025-02-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitorrecord',
            name='store_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
