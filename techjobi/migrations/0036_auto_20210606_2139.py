# Generated by Django 3.2.3 on 2021-06-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techjobi', '0035_auto_20210606_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='application_view',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='company_view',
            field=models.IntegerField(blank=True),
        ),
    ]