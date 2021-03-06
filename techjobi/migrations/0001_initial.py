# Generated by Django 3.1.4 on 2021-05-14 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=255)),
                ('job_type', models.CharField(choices=[('Full Time', 'Full Time'), ('Freelance', 'Freelance'), ('Part Time', 'Part Time'), ('Temporary', 'Temporary')], max_length=50)),
                ('job_category', models.CharField(choices=[('IT', 'IT'), ('Digital Banking', 'Digital Banking')], max_length=20)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('salary1', models.FloatField(blank=True)),
                ('salary2', models.FloatField(blank=True)),
                ('tags', models.CharField(blank=True, max_length=255)),
                ('job_description', models.CharField(blank=True, max_length=255)),
                ('file_upload', models.FileField(blank=True, upload_to='')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
