# Generated by Django 2.2.1 on 2019-06-03 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='alert_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
