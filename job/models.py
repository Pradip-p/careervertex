from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def total_job_count(self):
        return self.jobs.filter(is_publish=True).count() 
        
class Job(models.Model):
    uuid = models.CharField(max_length=50, null=True, blank=True, unique=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(help_text="Slug should be jobTitle-company-name-jobLocation-todayDate",unique=True,max_length=255)
    short_text = models.TextField()
    content = CKEditor5Field('Content', config_name='extends')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='job_images')
    pdf = models.FileField(upload_to='job_pdfs', null=True, blank=True)
    scrape_link = models.CharField(max_length =250, null=True, blank=True )
    is_publish = models.BooleanField(default=False)
    company_name = models.CharField(max_length = 250)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self._update_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.created_at.year), str(self.created_at.month), str(self.slug)])
    
    def _update_slug(self):
        if not self.slug:
            base_slug = slugify(self.title)
            
            # Include company name if available
            if self.company_name:
                base_slug += "-" + slugify(self.company_name)
        
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

            unique_slug = f"{base_slug}-{timestamp}"
                        
            while Job.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{timestamp_part}"
                timestamp_part += 1 

            self.slug = unique_slug


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
@receiver(post_save, sender=Contact)
def send_contact_email(sender, instance, created, **kwargs):
    if created:
        # Get all admin users' emails
        admin_emails = ['thapapradip542@gmail.com']
        # Send email
        send_mail(
            subject=f'New Contact: {instance.subject}',
            message=f'You have a new contact from {instance.name}.\n\nEmail: {instance.email} \n\nMessage:\n{instance.message}',
            from_email= instance.email,
            recipient_list=admin_emails,
        )