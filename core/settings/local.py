from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# Local specific settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
