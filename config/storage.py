import os
from urllib.parse import urljoin
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image

class CustomStorage(FileSystemStorage):
    '''Custom storage for django_ckeditor_5 images.'''
    location = os.path.join(settings.MEDIA_ROOT,"ckeditor")
    base_url = urljoin(settings.MEDIA_URL, "ckeditor/")
    
    def save(self, name, content, max_size=(600, 700)):
        '''Override save method to resize images before saving.'''
        # Save the original image
        saved_name = super().save(name, content)

        # Get the full path to the saved image
        image_path = os.path.join(self.location, saved_name)

        # Open the image file
        with open(image_path, 'rb') as f:
            img = Image.open(f)

            # Resize the image
            img.thumbnail(max_size)

            # Save the resized image, overwriting the original file
            img.save(image_path)

        return saved_name
    