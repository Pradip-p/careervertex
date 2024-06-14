from django import template
from job.models import Job, Category

register = template.Library()

@register.simple_tag
def get_categories():
    try:
        # Fetching categories ordered by name
        categories = Category.objects.all().order_by('id')
    except Category.DoesNotExist:
        categories = []
    return categories

@register.simple_tag
def get_recent_jobs():
    try:
        jobs = Job.objects.filter(is_publish = True ).order_by('-created_at')[:4]
    except Job.DoesNotExist:
        jobs = []
    return jobs