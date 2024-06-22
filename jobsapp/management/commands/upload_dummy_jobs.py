# your_app/management/commands/upload_dummy_jobs.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from jobsapp.models import Job, Tag, User
from django.contrib.auth.hashers import make_password
import random

class Command(BaseCommand):
    help = 'Uploads dummy job data'

    def handle(self, *args, **kwargs):
        # Create a dummy user
        user_data = {
            'email': f'dummy@example_{random.randint(1,100)}.com',
            'password': make_password('password123'),  # Hash the password
            'role': 'employee',
            'gender': 'male',
        }
        user = User.objects.create(**user_data)

        # Generate 100 dummy jobs
        dummy_jobs = []
        for i in range(1, 101):
            job_data = {
                'user': user,
                'title': f'Dummy Job {i}',
                'description': f'Description of Dummy Job {i}',
                'location': f'Dummy Location {random.randint(1, 5)}',
                'type': random.choice(['Full-time', 'Part-time', 'Contract']),
                'category': f'Category {random.randint(1, 10)}',
                'last_date': timezone.now() + timezone.timedelta(days=random.randint(1, 30)),
                'company_name': f'Dummy Company {random.randint(1, 20)}',
                'company_description': f'Description of Dummy Company {random.randint(1, 20)}',
                'website': f'https://www.dummycompany{i}.com',
                'salary': random.randint(30000, 100000),
                'vacancy': random.randint(1, 5),
            }
            dummy_jobs.append(job_data)

        # Insert dummy jobs into the database
        for job_data in dummy_jobs:
            tags = Tag.objects.all().order_by('?')[:random.randint(1, 3)]  # Get random 1-3 tags
            job = Job.objects.create(
                user=job_data['user'],
                title=job_data['title'],
                description=job_data['description'],
                location=job_data['location'],
                type=job_data['type'],
                category=job_data['category'],
                last_date=job_data['last_date'],
                company_name=job_data['company_name'],
                company_description=job_data['company_description'],
                website=job_data['website'],
                salary=job_data['salary'],
                vacancy=job_data['vacancy'],
            )
            job.tags.add(*tags)  # Add tags to the job

        self.stdout.write(self.style.SUCCESS('Successfully uploaded 100 dummy jobs'))
