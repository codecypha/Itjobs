# Generated by Django 3.2.3 on 2021-06-07 13:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('techjobi', '0038_auto_20210607_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='deadline',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
