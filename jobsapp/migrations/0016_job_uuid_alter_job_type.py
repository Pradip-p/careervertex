# Generated by Django 4.0.1 on 2024-06-23 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0015_job_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='uuid',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship'), ('4', 'Contract')], max_length=10),
        ),
    ]
