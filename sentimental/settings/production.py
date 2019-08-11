from sentimental.settings.common import *
import os

DEBUG = True

SECRET_KEY = 'DwuJyCBYF5kL9JjLILg47TCZKLWQ6LsA'

ALLOWED_HOSTS = ['insects.space']

CSRF_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'insects',
        'USER': 'postgres',
        'PASSWORD': 'ggkFhhZCD9yGJwsd',
        'HOST': 'localhost',
    }
}