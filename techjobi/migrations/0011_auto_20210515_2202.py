# Generated by Django 3.1.4 on 2021-05-15 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techjobi', '0010_auto_20210515_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_category',
            field=models.CharField(choices=[('IT', 'IT'), ('Digital', 'Digital ')], max_length=100),
        ),
    ]
