# Generated by Django 3.2.3 on 2021-06-02 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techjobi', '0013_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]