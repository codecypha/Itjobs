# Generated by Django 3.2.3 on 2021-06-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techjobi', '0039_jobpost_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
