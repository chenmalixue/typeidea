from .base import *

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cxDB',
        'USER': 'root',
        'PASSWORD': 'information:168',
        'HOST': '192.168.138.8',
        'PORT': '3306',
    }
}