from django.urls import re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.flatpages import views as flatpages_views
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from config.sitemaps import Sitemaps, StaticViewSitemap



lang_patterns = i18n_patterns(path("", include("jobsapp.urls")),
                              path("", include("accounts.urls")),
                              )

urlpatterns = lang_patterns + [
    re_path(r"^i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("sitemap.xml/", sitemap, {"sitemaps": dict(Sitemaps())}, name="django.contrib.sitemaps.views.sitemap"),
]

if settings.ENABLE_PROMETHEUS:
    urlpatterns.append(path("", include('django_prometheus.urls')))

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
