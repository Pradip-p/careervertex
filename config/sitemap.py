from django.contrib.sitemaps import GenericSitemap


class PaginatedSitemap(GenericSitemap):
    limit = 20  
    
    def get_urls(self, page=1, site=None, **kwargs):
        urls = super().get_urls(page, site, **kwargs)
        for url in urls:
            url['changefreq'] = 'daily'  # Set the changefreq for each URL
        return urls

# class jobPostSitemap(Sitemap):
#     changefreq = 'daily'
#     priority = 0.9

#     def items(self):
#         return job.objects.filter(is_publish=True).order_by('-created_at')

#     def lastmod(self, obj):
#         return obj.created_at
