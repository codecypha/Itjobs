# Generated by Django 3.2.3 on 2021-06-06 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techjobi', '0036_auto_20210606_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='application_view',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company_view',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
