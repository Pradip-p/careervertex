import json
import hashlib
import os
import django
from django.core.files.base import ContentFile
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# settings.configure()
django.setup()
from job.models import Job, Category

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
            category_name = 'Ngo/Ingo jobs'  # Default category name
            category, created = Category.objects.get_or_create(name=category_name)
            
            Job.objects.create(
                uuid=item['jobkey'],
                title=item['job_title'],
                content = item['content'],
                category=category,
                scrape_link = item['scrape_link'],
                company_name = item['company_name']
            )
            print('Added to the Django SQLite database.........................')
