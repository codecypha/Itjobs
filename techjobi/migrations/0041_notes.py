# Generated by Django 3.2.3 on 2021-06-07 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techjobi', '0040_auto_20210607_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255)),
                ('priority', models.CharField(blank=True, max_length=255)),
                ('note', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'notes',
            },
        ),
    ]