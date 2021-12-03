# Generated by Django 3.2.3 on 2021-06-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techjobi', '0041_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='priority',
            field=models.CharField(choices=[('Low Priority', 'Low Priority'), ('Medium Priority', 'Medium Priority'), ('Medium Priority', 'Medium Priority')], max_length=50),
        ),
    ]