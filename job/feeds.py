from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Job

class LatestjobsFeed(Feed):
    title = "Career Links Nepal"
    link = "/job/"
    description = "Latest posts from my job"

    def items(self):
        return Job.objects.filter(is_publish=True).order_by('-created_at')[:50]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('job_detail', args=[str(item.created_at.year), str(item.created_at.month), str(item.slug)])