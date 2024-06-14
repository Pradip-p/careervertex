# Generated by Django 5.0.4 on 2024-05-05 10:16

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(help_text='Slug should be jobTitle-company-name-jobLocation-todayDate', max_length=255, unique=True)),
                ('short_text', models.TextField()),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='job_images')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='job_pdfs')),
                ('scrape_link', models.CharField(blank=True, max_length=250, null=True)),
                ('is_publish', models.BooleanField(default=False)),
                ('company_name', models.CharField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='job.category')),
            ],
        ),
    ]