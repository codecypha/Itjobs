# Generated by Django 3.2.3 on 2021-06-02 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techjobi', '0014_profile_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('company_description', models.TextField(blank=True)),
                ('file_upload', models.FileField(blank=True, upload_to='')),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]