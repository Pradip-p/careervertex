from django.urls import path

from job.feeds import LatestjobsFeed
from . import views

urlpatterns = [
    path("", views.home, name="jobs"),
    path('category/<slug:slug>/', views.category_detail, name='category-detail'),
    path('<int:year>/<int:month>/<slug:slug>/', views.job_detail, name='job_detail'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('terms/', views.terms_condition, name='terms'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('about-us/', views.about_us, name="about_us"),
    path("ads.txt", views.ads_txt_view,name="ads_txt"),
    path('feed/rss/', LatestjobsFeed(), name='rss_feed'),
    path('feed/atom/', LatestjobsFeed(), name='atom_feed'),
    path('search/', views.job_search, name='job_search'),
]