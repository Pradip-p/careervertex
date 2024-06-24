# your_app/management/commands/upload_dummy_jobs.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from job.models import Job, Tag, User
from django.contrib.auth.hashers import make_password
import random
import faker

class Command(BaseCommand):
    help = 'Uploads dummy job data'

    def handle(self, *args, **kwargs):
        """
        This command generates and uploads dummy job data into the database.
        
        It creates a dummy user and then generates 100 dummy jobs, each with
        various randomly generated attributes such as title, description, location,
        job type, category, last date, company name, company description, website, salary,
        and vacancy. It also assigns random tags to each job from existing tags in the database.
        
        After successfully uploading all the dummy jobs, it prints a success message.
        """
        fake = faker.Faker()
        
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
                'user': user,  # Assign the dummy user to each job
                'title': f'Dummy Job {i}',  # Unique title for each job
                'description': fake.paragraph(nb_sentences=40, variable_nb_sentences=True),  # Fake description
                'location': f'Dummy Location {random.randint(1, 5)}',  # Random location
                'type': random.choice(['Full-time', 'Part-time', 'Contract']),  # Random job type
                'category': f'Category {random.randint(1, 10)}',  # Random category
                'last_date': timezone.now() + timezone.timedelta(days=random.randint(1, 30)),  # Random last date
                'company_name': f'Dummy Company {random.randint(1, 20)}',  # Random company name
                'company_description': fake.paragraph(nb_sentences=3, variable_nb_sentences=True),  # Fake company description
                'website': f'https://www.dummycompany{i}.com',  # Company website
                'salary': random.randint(30000, 100000),  # Random salary
                'vacancy': random.randint(1, 5),  # Random number of vacancies
            }
            dummy_jobs.append(job_data)  # Append each job data to the list

        # Insert dummy jobs into the database
        for job_data in dummy_jobs:
            tags = Tag.objects.all().order_by('?')[:random.randint(1, 3)]  # Get random 1-3 tags from existing tags
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
            job.tags.add(*tags)  # Assign tags to the current job

        self.stdout.write(self.style.SUCCESS('Successfully uploaded 100 dummy jobs'))  # Success message
