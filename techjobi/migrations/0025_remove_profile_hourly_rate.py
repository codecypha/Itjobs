# Generated by Django 3.2.3 on 2021-06-05 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techjobi', '0024_auto_20210605_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='hourly_rate',
        ),
    ]
