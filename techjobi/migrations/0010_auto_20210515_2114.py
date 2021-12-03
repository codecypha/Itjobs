# Generated by Django 3.1.4 on 2021-05-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techjobi', '0009_auto_20210515_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_category',
            field=models.CharField(choices=[('Web & Software Dev', 'Web & Software Dev'), ('Data Science & Analitycs', 'Data Science & Analitycs'), ('Networking', 'Networking'), ('Support specialist', 'Support specialist'), ('Software Tester', 'Software Tester'), ('Analyst', 'Analyst'), ('User experience designer', 'User experience designer')], max_length=100),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Temporary', 'Temporary')], max_length=50),
        ),
    ]
