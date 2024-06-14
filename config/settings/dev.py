from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']
# settings.py

INTERNAL_IPS = [
    '127.0.0.1',
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}