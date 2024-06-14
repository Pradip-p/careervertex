from django.contrib import admin
from .models import Job, Category, Contact
from django.contrib.auth.models import Group,User
from django import forms
from django.utils.html import format_html
admin.site.unregister(Group)
admin.site.unregister(User)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','message')

        
admin.site.register(Contact, ContactAdmin)

class jobAdminForm(forms.ModelForm):
    class Meta:
        model = Job    
        fields = '__all__'

class JobAdmin(admin.ModelAdmin):
    form = jobAdminForm
    list_display = ('title','category','is_publish','scrape_link', 'created_at', 'display_image')
    exclude = ('uuid', 'pdf', 'scrape_link','company_name')
    list_per_page = 20  # Change this value according to your preference
    ordering = ('-created_at',)  # Ordering jobs by created_at in descending order
    search_fields = ['title']  # Adding search functionality for the 'title' field



    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50px" height="50px" />'.format(obj.image.url))
        else:
            return 'No Image'
    display_image.allow_tags = True
    display_image.short_description = 'Image'

class CategoryAdmin(admin.ModelAdmin):
    pass
    # exclude = ('slug',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Job, JobAdmin)


