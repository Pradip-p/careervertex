from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config.sitemap import PaginatedSitemap
from .robots import RobotsTxtView
from django.conf.urls import handler404, handler500
from job.views import custom_404, custom_500
from job.models import Job
from django.contrib.sitemaps import views as sitemaps_views

info_dict = {
    "queryset": Job.objects.filter(is_publish=True).order_by('-created_at'),
    "date_field": "created_at",
}

sitemaps = {"jobs": PaginatedSitemap(info_dict, priority=1.0)}

urlpatterns = [
    path('roleadmin/', admin.site.urls),
    path('', include('job.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('robots.txt', RobotsTxtView.as_view(), name='robots_txt'),
    path("sitemap.xml", 
        sitemaps_views.index,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.index"
    ),
    path("sitemap-<section>.xml", 
        sitemaps_views.sitemap, 
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap"
    ),
]
# Serve media files during development
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = custom_404
handler500 = custom_500
admin.site.site_header = 'Admin Dashboard'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'Admin Dashboard' # default: "Django site admin"