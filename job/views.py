import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from config import settings
from .models import Job, Category, Contact
from job.pagination import paginate_queryset

@cache_page(60 * 2)
def job_search(request):
    query = request.GET.get('q')
    if query:
        jobs = Job.objects.filter(title__icontains=query, is_publish=True).order_by('-created_at')
    else:
        jobs = Job.objects.filter(is_publish=True).order_by('-created_at')
    paginated_jobs = paginate_queryset(request, jobs)
    context = {'jobs': paginated_jobs}
    return render(request, 'job/index.html', context)

@cache_page(60 * 2)
def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    jobs = category.jobs.filter(is_publish=True).order_by('-created_at')
    paginated_jobs = paginate_queryset(request, jobs)
    context = {'jobs': paginated_jobs, 'category': category}
    return render(request, 'job/category.html', context)

@cache_page(60 * 2)
def home(request):
    jobs = Job.objects.filter(is_publish=True).order_by('-created_at')
    paginated_jobs = paginate_queryset(request, jobs)
    context = {'jobs': paginated_jobs}
    return render(request, 'job/index.html', context)

@cache_page(60 * 2)
def job_detail(request, year, month, slug):
    job = Job.objects.get(slug = slug)
    context = {'job': job}
    return render(request, 'job/single-post.html', context)

@cache_page(60 * 2)
def about_us(request):
    return render(request, 'job/about.html')

@cache_page(60 * 2)
def terms_condition(request):
    return render(request, 'job/terms.html')
@cache_page(60 * 2)
def privacy_policy(request):
    return render(request, 'job/privacy_policy.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Save the contact form data
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        success_message = "Thank you for reaching out! Our team will contact you soon."

        return render(request, 'job/contact.html',{'success_message': success_message})

    return render(request, 'job/contact.html')

def ads_txt_view(request):
    with open(os.path.join(settings.BASE_DIR, 'ads.txt')) as file:
        file_content = file.readlines()
    return HttpResponse(file_content, content_type="text/plain")

def custom_404(request, exception):
    return render(request, 'job/404.html', status=404)

def custom_500(request):
    return render(request, 'job/500.html', status=500)
