import json
import hashlib
import os
import django
from django.core.files.base import ContentFile
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobs.settings")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# settings.configure()
django.setup()
from jobsapp.models import Job, Tag
from accounts.models import User
from datetime import datetime
from dateutil import parser
import dateparser

class jobPipeline(object):

    def process_item(self, item, spider):
        hash_dict = {'job_title': item.get('job_title'), 'company_name': item.get('company_name')}
        binary = json.dumps(hash_dict).encode('utf-8')
        hashed_key = hashlib.sha1(binary).hexdigest()

        if 'jobkey' not in list(item.keys()):
            item['jobkey'] = hashed_key
        # Check if the jobkey already exists in the database
        try:
            existing_job = Job.objects.get(uuid = item['jobkey'])
        except Job.DoesNotExist:
            existing_job = None

        if existing_job:
            print(f"Job with key {hashed_key} already exists in the database. Skipping...")
        else:
            # Create the Job object
            category_name = 'Ngo/Ingo jobs'  # Default category name
            tags = Tag.objects.all()
            user = User.objects.order_by('-id').first()
            print(user)
            # Convert the string to a datetime object
            last_date_str = item['last_date']
            # Convert the string to a datetime object
            try:
                # Use dateparser to parse the datetime string
                last_date = dateparser.parse(last_date_str)
                if last_date:
                    # Convert to a datetime object (if it's not already)
                    if not isinstance(last_date, datetime):
                        last_date = last_date.replace(tzinfo=None)
            except Exception as e:
                # Handle parsing errors
                print(f"Error parsing last_date_str: {e}")
                last_date = None  # or provide a default datetime value


            if last_date:
                job = Job.objects.create(
                    uuid=item['jobkey'],
                    title=item['job_title'],
                    description=item['content'],
                    category=category_name,
                    # scrape_link=item['scrape_link'],
                    company_name=item['company_name'],
                    company_description=item['company_description'],
                    location=item['location'],
                    last_date = last_date,
                    type="1",
                    user = user
                    
                )

                # Set the tags for the job using .set()
                job.tags.set(tags)

                # Set the user for the job
                job.save()  # Save the job object after setting tags and user

                print('Added to the Django SQLite database.........................')
