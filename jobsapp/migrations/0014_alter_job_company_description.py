# Generated by Django 4.0.1 on 2024-06-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0013_job_vacancy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company_description',
            field=models.TextField(),
        ),
    ]
